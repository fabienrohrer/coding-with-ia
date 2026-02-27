#!/usr/bin/env python3
"""
Convert a Markdown file to PDF.

Usage:
    python scripts/md_to_pdf.py TP/input.md output.pdf
    python scripts/md_to_pdf.py TP/input.md out/output.pdf --title "My TP"
    python scripts/md_to_pdf.py --help
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from html import escape

try:
    import markdown as md_lib
except ImportError:
    md_lib = None

try:
    from weasyprint import HTML, CSS
except ImportError:
    HTML = None
    CSS = None


DEFAULT_CSS = """
@page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #222;
}

h1, h2, h3, h4, h5, h6 {
    color: #111;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
    line-height: 1.2;
}

h1 {
    font-size: 22pt;
    border-bottom: 2px solid #ddd;
    padding-bottom: 0.2em;
}

h2 {
    font-size: 16pt;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.15em;
}

h3 { font-size: 13pt; }

p, ul, ol {
    margin-top: 0.4em;
    margin-bottom: 0.7em;
}

ul, ol {
    padding-left: 1.4em;
}

code {
    font-family: "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace;
    font-size: 0.95em;
    background: #f5f5f5;
    padding: 0.08em 0.25em;
    border-radius: 3px;
}

pre {
    background: #f7f7f7;
    border: 1px solid #e6e6e6;
    border-radius: 6px;
    padding: 10px 12px;
    overflow-wrap: anywhere;
    white-space: pre-wrap; /* safer for PDF */
}

pre code {
    background: transparent;
    padding: 0;
    border-radius: 0;
}

blockquote {
    margin: 0.8em 0;
    padding: 0.4em 0.8em;
    border-left: 4px solid #ddd;
    background: #fafafa;
    color: #444;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.8em 0;
    font-size: 10.5pt;
}

th, td {
    border: 1px solid #ddd;
    padding: 6px 8px;
    vertical-align: top;
}

th {
    background: #f2f2f2;
    text-align: left;
}

img {
    max-width: 100%;
    height: auto;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 1.2em 0;
}
"""


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file (.md) to PDF.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input_md",
        type=Path,
        help="Path to the input Markdown file (.md)",
    )
    parser.add_argument(
        "output_pdf",
        type=Path,
        help="Path to the output PDF file (.pdf)",
    )
    parser.add_argument(
        "--title",
        type=str,
        default=None,
        help="Optional HTML document title (metadata only)",
    )
    parser.add_argument(
        "--css",
        type=Path,
        default=None,
        help="Optional path to a custom CSS file for PDF styling",
    )
    return parser


def ensure_dependencies() -> None:
    missing = []
    if md_lib is None:
        missing.append("markdown")
    if HTML is None or CSS is None:
        missing.append("weasyprint")
    if missing:
        print(
            "Missing Python dependencies: " + ", ".join(missing) + "\n"
            "Install them with:\n"
            "  pip install markdown weasyprint",
            file=sys.stderr,
        )
        sys.exit(2)


def read_markdown_file(path: Path) -> str:
    if not path.exists():
        print(f"Input file not found: {path}", file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f"Input path is not a file: {path}", file=sys.stderr)
        sys.exit(1)
    if path.suffix.lower() != ".md":
        print(f"Warning: input file does not have .md extension: {path}", file=sys.stderr)

    return path.read_text(encoding="utf-8")


def markdown_to_html(markdown_text: str, title: str | None = None) -> str:
    # Common useful extensions for workshop/TP style markdown
    html_body = md_lib.markdown(
        markdown_text,
        extensions=[
            "extra",       # tables, fenced code blocks, etc.
            "admonition",
            "toc",
            "sane_lists",
        ],
        output_format="html5",
    )

    safe_title = escape(title) if title else "Markdown Document"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{safe_title}</title>
</head>
<body>
{html_body}
</body>
</html>
"""


def write_pdf(
    html_string: str,
    output_pdf: Path,
    base_dir: Path,
    css_path: Path | None = None,
) -> None:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    stylesheets = []
    if css_path:
        if not css_path.exists():
            print(f"Custom CSS file not found: {css_path}", file=sys.stderr)
            sys.exit(1)
        stylesheets.append(CSS(filename=str(css_path)))
    else:
        stylesheets.append(CSS(string=DEFAULT_CSS))

    # base_url is important so relative images/links in markdown can resolve
    HTML(string=html_string, base_url=str(base_dir)).write_pdf(
        target=str(output_pdf),
        stylesheets=stylesheets,
    )


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    ensure_dependencies()

    input_md: Path = args.input_md.resolve()
    output_pdf: Path = args.output_pdf.resolve()
    css_path: Path | None = args.css.resolve() if args.css else None

    markdown_text = read_markdown_file(input_md)
    html_string = markdown_to_html(markdown_text, title=args.title)
    write_pdf(html_string, output_pdf, base_dir=input_md.parent, css_path=css_path)

    print(f"PDF generated successfully: {output_pdf}")


if __name__ == "__main__":
    main()
