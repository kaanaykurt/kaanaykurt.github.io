"""Render publication data from _data/publications.yml into the site's HTML.

Used by publications.qmd (full list) and cv.qmd (selected entries).
Markup matches publications.css / cv.css; keep class names in sync with those files.
"""

import html
from pathlib import Path

import yaml

ME = "K. Aykurt"


def load(path="_data/publications.yml"):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _esc(value):
    return html.escape(str(value), quote=True)


def _authors(authors):
    return ", ".join(
        f'<span class="me">{_esc(a)}</span>' if a == ME else _esc(a) for a in authors
    )


def _venue(pub):
    if pub.get("status") == "preprint":
        return _esc(pub["venue"])
    return f'{_esc(pub["venue"])}, {pub["year"]}'


def _title(pub):
    title = _esc(pub["title"])
    if pub.get("pdf"):
        return f'<a href="{_esc(pub["pdf"])}" target="_blank" rel="noopener">{title}</a>'
    return title


def _group(pub):
    return "Preprints" if pub.get("status") == "preprint" else str(pub["year"])


def _card(pub, n):
    out = [
        '<div class="pub-card">',
        f'<div class="pub-title">{_title(pub)}</div>',
        f'<div class="pub-authors">{_authors(pub["authors"])}</div>',
        f'<div class="pub-venue">{_venue(pub)}</div>',
    ]
    row, panels = [], []
    if pub.get("publisher"):
        row.append(
            f'<a class="pub-pill pub-link pub-publisher" href="{_esc(pub["publisher"])}" '
            'target="_blank" rel="noopener">'
            '<i class="bi bi-box-arrow-up-right" aria-hidden="true"></i> Publisher</a>'
        )
    if pub.get("abstract"):
        row.append(
            f'<button class="pub-pill pub-toggle" type="button" aria-expanded="false" '
            f'aria-controls="pub-abs-{n}"><i class="bi bi-file-text" aria-hidden="true"></i> '
            'Abstract <span class="pub-bib-arrow" aria-hidden="true">▾</span></button>'
        )
        paras = "".join(
            f"<p>{_esc(p.strip())}</p>" for p in pub["abstract"].split("\n\n") if p.strip()
        )
        panels.append(
            f'<div class="pub-abs-wrap pub-panel" id="pub-abs-{n}" hidden>'
            f'<div class="pub-abs-text">{paras}</div></div>'
        )
    if pub.get("bibtex"):
        row.append(
            f'<button class="pub-pill pub-toggle" type="button" aria-expanded="false" '
            f'aria-controls="pub-bib-{n}"><i class="bi bi-code-slash" aria-hidden="true"></i> '
            'BibTeX <span class="pub-bib-arrow" aria-hidden="true">▾</span></button>'
        )
        panels.append(
            f'<div class="pub-bibtex-wrap pub-panel" id="pub-bib-{n}" hidden>'
            '<button class="pub-bib-copy" type="button" aria-label="Copy BibTeX">'
            '<i class="bi bi-clipboard"></i></button>\n'
            f'<pre class="pub-bibtex">{_esc(pub["bibtex"].strip())}</pre></div>'
        )
    if row:
        out.append(
            '<div class="pub-links">'
            f'<div class="pub-link-row">{"".join(row)}</div>'
            f'<div class="pub-link-panels">{"".join(panels)}</div>'
            "</div>"
        )
    out.append("</div>")
    return "\n".join(out)


def publications_html(pubs):
    """Full list grouped by year (preprints first), in the order given in the data file."""
    groups = []
    for pub in pubs:
        label = _group(pub)
        if not groups or groups[-1][0] != label:
            groups.append((label, []))
        groups[-1][1].append(pub)
    out, n = ['<div class="pub-list">'], 0
    for label, items in groups:
        gid = f"pub-year-{label.lower()}"
        out.append(
            '<div class="pub-year-group">'
            f'<button class="pub-year-toggle is-open" type="button" aria-expanded="true" '
            f'aria-controls="{gid}"><span class="pub-year-label">{_esc(label)}</span></button>'
            f'<div class="pub-year-content" id="{gid}">'
        )
        for pub in items:
            n += 1
            out.append(_card(pub, n))
        out.append("</div></div>")
    out.append("</div>")
    return "\n".join(out)


def selected_html(pubs):
    """Compact list of entries marked `selected: true`, for the CV page."""
    out = ['<div class="cv-pubs">']
    for pub in pubs:
        if not pub.get("selected"):
            continue
        out.append(
            '<div class="cv-pub">'
            f'<div class="cv-pub-title">{_title(pub)}</div>'
            f'<div class="cv-pub-meta">{_authors(pub["authors"])}. {_venue(pub)}.</div>'
            "</div>"
        )
    out.append("</div>")
    return "\n".join(out)
