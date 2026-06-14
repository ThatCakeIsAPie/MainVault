# Audio Recording Processing Log

**Raw recordings (outside vault):** ~/Recordings-Raw/
**Compressed versions (in vault):** Research/raw/audio/
**Transcripts:** Research/raw/transcripts/
**Preferred STT:** Grok (xAI) — model: grok-stt

## Workflow
1. Obsidian records → `~/Recordings-Raw/`
2. Compress (mono, 16 kHz, 32 kbps):
   ```bash
   ffmpeg -y -i "input.m4a" -ac 1 -ar 16000 -b:a 32k "output-16k-32k.mp3"
   ```
3. Move compressed .mp3 into `Research/raw/audio/`
4. Cloud agent transcribes using Grok STT

## Current Files

| Original Date | Raw File (outside)                  | Compressed (in vault)              | Status  | Transcript |
|---------------|-------------------------------------|------------------------------------|---------|------------|
| 2026-06-11    | Recording 20260611220952.m4a       | Recording-20260611-16k-32k.mp3    | Pending | -          |
| 2026-06-13    | Recording 20260613173632.m4a       | Recording-20260613-16k-32k.mp3    | Pending | -          |

## Size Comparison
- 2026-06-11: 32 MB → 7.9 MB
- 2026-06-13: 108 MB → 27 MB
