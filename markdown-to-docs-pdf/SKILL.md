---
name: markdown-to-docs-pdf
description: Convert Markdown files to professional DOCX or PDF documents using Pandoc via a bundled script. Use when a user asks to turn Markdown into Word/PDF, convert a .md into a document, or export Markdown to a file (docx/pdf only, no HTML).
---

# Markdown To Docs Pdf

## Overview
Convert Markdown into a decent DOCX or PDF with a single script. Use `uvx` to run the script with `pypandoc-binary` so Pandoc is available without a system install.

## Quick Start
DOCX:
```bash
uvx --from pypandoc-binary python scripts/convert_markdown.py input.md --to docx
```

PDF:
```bash
uvx --from pypandoc-binary python scripts/convert_markdown.py input.md --to pdf
```

## Workflow
1. Confirm the input Markdown path and target format (`docx` or `pdf`).
2. Decide whether styling is needed:
   - For DOCX styling, ask for a reference DOCX and pass `--reference-doc`.
   - For PDF rendering issues, try a specific engine via `--pdf-engine` if available.
3. Run the script (prefer `uvx` + `pypandoc-binary` for a self-contained Pandoc).
4. Check the output file and re-run with options (`--toc`, `--metadata`, `--reference-doc`) if needed.

## Script Reference
Use `scripts/convert_markdown.py`.

Arguments:
- `input`: Markdown file path.
- `--to docx|pdf`: Target format.
- `--output`: Output path (optional; defaults to same name with new extension).
- `--reference-doc`: DOCX template for styling.
- `--pdf-engine`: Pandoc PDF engine (e.g., `wkhtmltopdf`, `tectonic`).
- `--toc`: Include a table of contents.
- `--metadata key=value`: Repeatable metadata entries.

If Pandoc is already installed on the system, you can run the script directly with `python3`.
