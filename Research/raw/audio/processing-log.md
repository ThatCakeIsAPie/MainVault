# Audio Recording Processing Log

**Location:** Research/raw/audio/
**Transcripts:** Research/raw/transcripts/
**Preferred STT:** Grok (xAI) — model: grok-stt

## Compression Workflow (for large files)
```bash
ffmpeg -y -i "input.m4a" -ac 1 -ar 16000 -b:a 32k "output-16k-32k.mp3"
```
- Typical reduction: ~75% (108 MB → ~27 MB)

## Processed Recordings

| Date       | Filename                              | Status     | Transcript File                          | Notes |
|------------|---------------------------------------|------------|------------------------------------------|-------|
| 2026-06-11 | Recording 20260611220952.m4a         | Done       | 2026-06-11 — LTD Amway Info Session...   | Already transcribed |
| 2026-06-13 | Recording 20260613173632.m4a         | Pending    | -                                        | Use compression + Grok STT |

## Notes
- Raw audio files are kept in this folder
- For files > ~50 MB, compress first before transcription or committing
