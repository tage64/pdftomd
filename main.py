import argparse
from pathlib import Path

import pymupdf.layout


def pdftomd(pdf_file: Path, md_file: Path):
    pymupdf.layout.activate()
    import pymupdf4llm

    md_text = pymupdf4llm.to_markdown(pdf_file)  # get markdown for all pages
    md_file.write_bytes(md_text.encode(encoding="utf-8", errors="replace"))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("pdf_file", type=Path, help="path to the pdf file")
    argparser.add_argument(
        "markdown_file",
        nargs="?",
        type=Path,
        help="the output markdown file  (defaults to the input file with extension replaced to .md",
    )
    args = argparser.parse_args()

    pdf_file = args.pdf_file
    md_file = args.markdown_file or pdf_file.with_suffix(".md")
    print(f"Converting {pdf_file} to {md_file}...")
    pdftomd(pdf_file, md_file)
    print("Done!")


if __name__ == "__main__":
    main()
