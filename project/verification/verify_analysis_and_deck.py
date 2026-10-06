#!/usr/bin/env python3
"""Check the analysis modules and the dependency-free presentation prototype."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ANALYSIS = PROJECT / "analysis"
DECK = PROJECT / "presentation" / "baseline"


class HTMLReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.refs: list[str] = []
        self.viewport = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        values = dict(attrs)
        if tag == "meta" and values.get("name") == "viewport":
            self.viewport = True
        for key in ("href", "src"):
            value = values.get(key)
            if value:
                self.refs.append(value)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL {message}")


def check_files() -> None:
    required = [
        ANALYSIS / "README.md",
        ANALYSIS / "00-cadre-et-methode.md",
        ANALYSIS / "01-cadrage-perimetre-planning.md",
        ANALYSIS / "02-gouvernance-interfaces.md",
        ANALYSIS / "03-registre-integre-des-risques.md",
        ANALYSIS / "04-traitements-continuite-apprentissage.md",
        ANALYSIS / "05-lecture-critique-limites.md",
        PROJECT / "presentation" / "brief.md",
        DECK / "index.html",
        DECK / "styles.css",
        DECK / "app.js",
        DECK / "demo-spec.json",
    ]
    for path in required:
        if not path.is_file() or not path.stat().st_size:
            fail(f"missing or empty file: {path}")


def check_markdown() -> None:
    files = sorted(ANALYSIS.glob("*.md")) + [PROJECT / "presentation" / "brief.md"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        if re.search(r"\\\[\s*.+?\s*\\\]", text, flags=re.DOTALL):
            fail(f"formula uses bracket delimiters: {path}")
        for match in re.finditer(r"\\times", text):
            if text[: match.start()].count("$") % 2 == 0:
                fail(f"LaTeX command is outside dollar delimiters: {path}")
        for reference in re.findall(r"\]\(([^)]+)\)", text):
            if reference.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (path.parent / reference.split("#", 1)[0]).resolve()
            if not target.is_file():
                fail(f"broken Markdown reference in {path}: {reference}")


def check_deck() -> None:
    html_path = DECK / "index.html"
    source = html_path.read_text(encoding="utf-8")
    parser = HTMLReferences()
    parser.feed(source)
    if not {"html", "title", "main", "section"}.issubset(parser.tags):
        fail("deck lacks required semantic elements")
    if not parser.viewport:
        fail("deck lacks a viewport declaration")
    if 'class="matrix"' not in source or "<table>" not in source:
        fail("deck lacks its matrix or evidence table")
    for reference in parser.refs:
        if reference.startswith(("http://", "https://", "//", "/", "file:")):
            fail(f"unsafe or remote reference: {reference}")
        if reference.startswith("#"):
            continue
        target = (DECK / reference.split("#", 1)[0]).resolve()
        if not target.is_file():
            fail(f"broken deck reference: {reference}")
    css = (DECK / "styles.css").read_text(encoding="utf-8")
    if css.count("{") != css.count("}") or "@import" in css.lower():
        fail("CSS is malformed or imports external resources")
    spec = json.loads((DECK / "demo-spec.json").read_text(encoding="utf-8"))
    if spec.get("mode") != "hybrid" or spec.get("complexity") != "standard":
        fail("demo spec does not describe the selected mode")
    if not spec.get("learning_objective"):
        fail("demo spec has no learning objective")


def main() -> int:
    check_files()
    check_markdown()
    check_deck()
    print("OK analysis modules and baseline deck")
    return 0


if __name__ == "__main__":
    sys.exit(main())
