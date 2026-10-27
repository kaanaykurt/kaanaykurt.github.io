"""Quarto post-render hook: fix markup Quarto emits that fails accessibility audits.

Runs after every `quarto render` (see `post-render` in _quarto.yml). Quarto passes the
rendered files in QUARTO_PROJECT_OUTPUT_FILES, one path per line.
"""

import os
import re
from pathlib import Path

# The navbar hamburger is a <button>; Quarto adds role="menu", which ARIA forbids on buttons.
TOGGLER_ROLE = re.compile(r'(<button class="navbar-toggler"[^>]*?) role="menu"')


def main():
    files = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").splitlines()
    fixed = 0
    for name in files:
        path = Path(name)
        if path.suffix != ".html" or not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        new = TOGGLER_ROLE.sub(r"\1", html)
        if new != html:
            path.write_text(new, encoding="utf-8")
            fixed += 1
    print(f"postrender: removed role=menu from the navbar toggler in {fixed} file(s)")


if __name__ == "__main__":
    main()
