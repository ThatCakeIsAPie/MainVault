#!/usr/bin/env python3
"""Read-only Obsidian vault validator for Research wiki + OKF hygiene.

Scans markdown files; reports issues. Stdlib only. Always exits 0 (report mode).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Directories excluded from note checks
EXCLUDE_DIRS = {".obsidian", ".git", "_tools"}

# Research paths with special rules
RESEARCH_PREFIX = "Research/"
RAW_PREFIX = "Research/raw/"
WIKI_SKIP_BASENAMES = {
    "index",
    "log",
    "schema",
    "source-manifest",
    "okf-compatibility",
    "validation-report",
    "processed-sources",
}

# Docs with example wikilinks / self-referential noise — still secret-scanned, no unresolved_link
LINK_RESOLUTION_SKIP_PATHS = {
    "CLAUDE.md",
    "Research/SCHEMA.md",
    "Research/SOURCE-MANIFEST.md",
    "Research/OKF-COMPATIBILITY.md",
    "Research/VALIDATION-REPORT.md",
    "Research/log.md",
    "Research/index.md",
}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("BEGIN PRIVATE KEY", re.compile(r"BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY", re.I)),
    ("sk-", re.compile(r"\bsk-[A-Za-z0-9]{20,}")),
    ("xoxb-", re.compile(r"\bxoxb-[A-Za-z0-9\-]+")),
    ("ghp_", re.compile(r"\bghp_[A-Za-z0-9]{20,}")),
    ("OPENAI_API_KEY=", re.compile(r"OPENAI_API_KEY\s*=\s*\S+")),
    ("ANTHROPIC_API_KEY=", re.compile(r"ANTHROPIC_API_KEY\s*=\s*\S+")),
    ("XAI_API_KEY=", re.compile(r"XAI_API_KEY\s*=\s*\S+")),
    ("ZEROENTROPY", re.compile(r"ZEROENTROPY[_A-Z]*\s*=\s*\S+", re.I)),
]

WIKI_REQUIRED_KEYS = ("title", "created", "updated", "type", "tags")
RAW_REQUIRED_KEYS = ("source_url", "ingested", "sha256")


@dataclass
class Issue:
    severity: str  # error | warning | info
    category: str
    path: str
    message: str
    line: int | None = None


@dataclass
class Report:
    vault_root: str
    scanned_files: int = 0
    issues: list[Issue] = field(default_factory=list)

    def add(self, issue: Issue) -> None:
        self.issues.append(issue)


def parse_simple_yaml_block(block: str) -> dict[str, Any]:
    """Minimal YAML frontmatter parser (key: value, lists on one line)."""
    data: dict[str, Any] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            if not inner:
                data[key] = []
            else:
                data[key] = [p.strip().strip("'\"") for p in inner.split(",")]
        else:
            data[key] = rest.strip("'\"") if rest else ""
    return data


def split_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return parse_simple_yaml_block(m.group(1)), text[m.end() :]


def normalize_wikilink_target(raw: str) -> str:
    """Strip alias (|) and heading (#); return link target for resolution."""
    target = raw.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    return target


def strip_code_for_wikilink_scan(text: str) -> str:
    """Remove fenced and inline code so documentation examples do not count as links."""
    out = text
    out = re.sub(r"```[\s\S]*?```", "", out)
    out = re.sub(r"`[^`\n]+`", "", out)
    return out


def should_skip_link_resolution(rel: str) -> bool:
    return rel in LINK_RESOLUTION_SKIP_PATHS


def is_excluded_path(rel: Path) -> bool:
    parts = rel.parts
    if not parts:
        return True
    if parts[0] in EXCLUDE_DIRS:
        return True
    for p in parts:
        if p in EXCLUDE_DIRS:
            return True
    return False


def rel_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_research_wiki_note(rel: str) -> bool:
    if not rel.startswith(RESEARCH_PREFIX) or not rel.endswith(".md"):
        return False
    if rel.startswith(RAW_PREFIX):
        return False
    if rel in (
        "Research/index.md",
        "Research/log.md",
        "Research/SCHEMA.md",
        "Research/SOURCE-MANIFEST.md",
        "Research/OKF-COMPATIBILITY.md",
        "Research/VALIDATION-REPORT.md",
    ):
        return False
    if "/raw/" in rel:
        return False
    if "/transcripts/" in rel.lower() and rel.startswith(RAW_PREFIX):
        return False
    # External AI Memory under Research — treat as wiki-adjacent but skip link threshold
    if "External AI Memory" in rel:
        return False
    return True


def is_raw_note(rel: str) -> bool:
    return rel.startswith(RAW_PREFIX) and rel.endswith(".md")


def is_link_threshold_note(rel: str) -> bool:
    if not is_research_wiki_note(rel):
        return False
    base = Path(rel).stem.lower()
    if base in WIKI_SKIP_BASENAMES:
        return False
    if "/transcripts/" in rel.lower():
        return False
    return True


def build_note_index(root: Path) -> dict[str, set[str]]:
    """Map lowercase basename (no ext) and full rel path stem to relative paths."""
    by_name: dict[str, set[str]] = defaultdict(set)
    for path in root.rglob("*.md"):
        rel = rel_posix(path, root)
        if is_excluded_path(Path(rel)):
            continue
        stem = path.stem.lower()
        by_name[stem].add(rel)
        # Also allow path-style links without extension
        rel_no_ext = rel[:-3] if rel.endswith(".md") else rel
        by_name[rel_no_ext.lower()].add(rel)
    return by_name


def resolve_link(target: str, by_name: dict[str, set[str]]) -> bool:
    t = target.strip()
    if not t:
        return False
    # External URLs in wikilinks are rare; treat as unresolved warning
    if re.match(r"^[a-z]+://", t, re.I):
        return True
    key = Path(t).stem.lower() if "/" in t or not t.endswith(".md") else t.lower()
    if t.lower() in by_name:
        return True
    if key in by_name:
        return True
    # path with folders
    no_ext = t.lower().removesuffix(".md")
    if no_ext in by_name:
        return True
    return False


def scan_secrets(report: Report, rel: str, lines: list[str]) -> None:
    for i, line in enumerate(lines, start=1):
        for label, pat in SECRET_PATTERNS:
            if pat.search(line):
                report.add(
                    Issue(
                        "warning",
                        "secret_scan",
                        rel,
                        f"Possible secret pattern: {label}",
                        i,
                    )
                )


def validate_file(
    report: Report,
    root: Path,
    path: Path,
    by_name: dict[str, set[str]],
) -> None:
    rel = rel_posix(path, root)
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        report.add(Issue("warning", "io", rel, f"Could not read: {e}"))
        return

    report.scanned_files += 1
    fm, body = split_frontmatter(text)
    lines = text.splitlines()
    scan_secrets(report, rel, lines)

    if is_research_wiki_note(rel):
        if fm is None:
            report.add(
                Issue("warning", "frontmatter", rel, "Missing YAML frontmatter")
            )
        else:
            for key in WIKI_REQUIRED_KEYS:
                if key not in fm or fm[key] in ("", None, []):
                    report.add(
                        Issue(
                            "warning",
                            "frontmatter",
                            rel,
                            f"Missing or empty frontmatter key: {key}",
                        )
                    )

    if is_raw_note(rel):
        if fm is None:
            report.add(
                Issue("info", "raw_frontmatter", rel, "No frontmatter on raw note")
            )
        else:
            for key in RAW_REQUIRED_KEYS:
                if key not in fm or (isinstance(fm[key], str) and not fm[key].strip()):
                    report.add(
                        Issue(
                            "warning",
                            "raw_frontmatter",
                            rel,
                            f"Missing or empty raw field: {key}",
                        )
                    )

    link_scan_text = strip_code_for_wikilink_scan(text)
    wikilinks = WIKILINK_RE.findall(link_scan_text)
    if is_link_threshold_note(rel):
        outbound = len(wikilinks)
        if outbound < 2:
            report.add(
                Issue(
                    "warning",
                    "wikilinks",
                    rel,
                    f"Fewer than 2 wikilinks (found {outbound})",
                )
            )

    if not should_skip_link_resolution(rel):
        for raw_link in wikilinks:
            target = normalize_wikilink_target(raw_link)
            if not target:
                continue
            if not resolve_link(target, by_name):
                report.add(
                    Issue(
                        "warning",
                        "unresolved_link",
                        rel,
                        f"Unresolved wikilink target: [[{raw_link}]]",
                    )
                )


def summarize(report: Report) -> dict[str, Any]:
    by_cat: dict[str, int] = defaultdict(int)
    by_sev: dict[str, int] = defaultdict(int)
    for iss in report.issues:
        by_cat[iss.category] += 1
        by_sev[iss.severity] += 1
    return {
        "vault_root": report.vault_root,
        "scanned_files": report.scanned_files,
        "issue_count": len(report.issues),
        "by_severity": dict(by_sev),
        "by_category": dict(sorted(by_cat.items(), key=lambda x: -x[1])),
    }


def format_markdown(report: Report, max_list: int = 80) -> str:
    summary = summarize(report)
    lines = [
        "# Vault Validation Report",
        "",
        f"**Vault:** `{report.vault_root}`",
        f"**Files scanned:** {summary['scanned_files']}",
        f"**Issues:** {summary['issue_count']}",
        "",
        "## Summary by severity",
        "",
    ]
    for sev, n in sorted(summary.get("by_severity", {}).items()):
        lines.append(f"- **{sev}:** {n}")
    lines.extend(["", "## Summary by category", ""])
    for cat, n in summary.get("by_category", {}).items():
        lines.append(f"- **{cat}:** {n}")
    lines.extend(["", "## Sample issues", ""])
    shown = 0
    for iss in report.issues:
        if shown >= max_list:
            lines.append(f"\n_(… {len(report.issues) - max_list} more issues omitted)_")
            break
        loc = f":{iss.line}" if iss.line else ""
        lines.append(
            f"- [{iss.severity}] **{iss.category}** — `{iss.path}`{loc}: {iss.message}"
        )
        shown += 1
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Obsidian vault (read-only)")
    parser.add_argument(
        "vault",
        nargs="?",
        default=".",
        help="Path to vault root (default: cwd)",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown", "text"),
        default="text",
        help="Output format",
    )
    parser.add_argument(
        "--max-list",
        type=int,
        default=80,
        help="Max issues listed in markdown output",
    )
    args = parser.parse_args()

    root = Path(args.vault).resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 0

    report = Report(vault_root=str(root))
    by_name = build_note_index(root)

    for path in sorted(root.rglob("*.md")):
        rel = rel_posix(path, root)
        if is_excluded_path(Path(rel)):
            continue
        validate_file(report, root, path, by_name)

    if args.format == "json":
        payload = {
            **summarize(report),
            "issues": [
                {
                    "severity": i.severity,
                    "category": i.category,
                    "path": i.path,
                    "message": i.message,
                    "line": i.line,
                }
                for i in report.issues
            ],
        }
        print(json.dumps(payload, indent=2))
    elif args.format == "markdown":
        print(format_markdown(report, max_list=args.max_list))
    else:
        s = summarize(report)
        print(f"Scanned {s['scanned_files']} files, {s['issue_count']} issues")
        for cat, n in s.get("by_category", {}).items():
            print(f"  {cat}: {n}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())