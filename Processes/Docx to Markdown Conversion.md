# Docx to Markdown Conversion

## Tool
**Pandoc** — installed via winget (`JohnMacFarlane.Pandoc`, v3.9.0.1)
Executable: `C:\Users\Lyle\AppData\Local\Pandoc\pandoc.exe`

## Command

### Single file
```bash
"/c/Users/Lyle/AppData/Local/Pandoc/pandoc.exe" "path/to/file.docx" -f docx -t gfm --wrap=none -o "path/to/output.md"
```

### Batch convert a folder
```bash
for f in "C:/Users/Lyle/Documents/Main Vault/Importer/Church Notes/"*.docx; do
  "/c/Users/Lyle/AppData/Local/Pandoc/pandoc.exe" "$f" -f docx -t gfm --wrap=none -o "${f%.docx}.md"
done
```

## Key flags
| Flag | Purpose |
|:---|:---|
| `-f docx` | Input format: Word document |
| `-t gfm` | Output format: GitHub Flavored Markdown (gives proper pipe tables) |
| `--wrap=none` | Prevents pandoc from hard-wrapping long lines |

## Notes
- Use `-t gfm` not `-t markdown` — the default markdown format produces space-aligned "simple tables" that Obsidian does not render correctly. GFM produces pipe tables (`| col | col |`) that render properly.
- Header rows in converted tables will be bold text rather than a true header row, but Obsidian renders them fine.
- Escaped dollar signs (`\$`) and apostrophes (`\'`) render correctly in Obsidian's preview mode.
- The **Docxer** plugin can convert files one at a time via the Obsidian UI (open file → click Convert button), but has no batch mode.
