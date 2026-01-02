#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys


def parse_metadata(items):
    metadata = []
    for item in items or []:
        if "=" not in item:
            raise ValueError(f"metadata '{item}' must be key=value")
        metadata.append(item)
    return metadata


def build_output_path(input_path, output, target):
    if output:
        return Path(output)
    return input_path.with_suffix(f".{target}")


def convert_markdown(input_path, output_path, target, reference_doc, pdf_engine, toc, metadata):
    try:
        import pypandoc
    except Exception as exc:
        raise RuntimeError("pypandoc is required. Try: uvx --from pypandoc-binary python scripts/convert_markdown.py ...") from exc

    extra_args = ["--from", "markdown", "--standalone"]
    if toc:
        extra_args.append("--toc")
    if reference_doc:
        extra_args.append(f"--reference-doc={reference_doc}")
    if pdf_engine:
        extra_args.append(f"--pdf-engine={pdf_engine}")
    for item in metadata:
        extra_args.extend(["-M", item])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pypandoc.convert_file(
        str(input_path),
        target,
        outputfile=str(output_path),
        extra_args=extra_args,
    )


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to DOCX or PDF using Pandoc.")
    parser.add_argument("input", help="Path to a Markdown file")
    parser.add_argument("--to", choices=["docx", "pdf"], required=True, help="Target format")
    parser.add_argument("--output", help="Output file path (optional)")
    parser.add_argument("--reference-doc", help="Path to a reference DOCX for styling")
    parser.add_argument("--pdf-engine", help="Pandoc PDF engine (e.g., wkhtmltopdf, tectonic)")
    parser.add_argument("--toc", action="store_true", help="Include a table of contents")
    parser.add_argument("--metadata", action="append", help="Metadata key=value (repeatable)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists() or not input_path.is_file():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    try:
        metadata = parse_metadata(args.metadata)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output_path = build_output_path(input_path, args.output, args.to)

    try:
        convert_markdown(
            input_path,
            output_path,
            args.to,
            args.reference_doc,
            args.pdf_engine,
            args.toc,
            metadata,
        )
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
