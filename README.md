# kaanaykurt.me

Source of my personal website, built with [Quarto](https://quarto.org) and served by GitHub Pages from the `docs/` folder on `main`.

## Layout

| Path | What it is |
| --- | --- |
| `index.qmd`, `cv.qmd`, `publications.qmd`, `teaching.qmd`, `blog.qmd` | The pages. Each has a matching `*.css`. |
| `_data/publications.yml` | All publications. `publications.qmd` and the CV's selected list are rendered from it by `_lib/pubs.py`. |
| `blogs/<date>_<slug>/blog.qmd` | Blog posts. Python cells are executed once and cached in `_freeze/`. |
| `theme.scss`, `styles.css`, `fonts/`, `theme-init.html`, `theme-toggle.js` | Theme, self-hosted fonts, and the light/dark toggle. |
| `docs/` | Rendered site. Committed, because GitHub Pages serves it directly. |
| `.devcontainer/` | Build environment: Quarto, Python, and TeX Live. |

## Building

Everything renders inside the dev container, so nothing needs to be installed locally except Docker. Either open the folder in VS Code and choose *Reopen in Container*, or run:

```bash
cd .devcontainer && docker compose run --rm dev bash -c 'cd /workspaces/website && quarto render'
```

Then commit the updated `docs/` and push. The site is live a minute later.

## Common edits

- **Add a paper:** append an entry to `_data/publications.yml`. Set `selected: true` to show it on the CV page, `status: preprint` to list it under Preprints.
- **Add a blog post:** create `blogs/YYYY-MM-DD_slug/blog.qmd` with `title`, `date`, `description` and `categories` in the front matter. Posts are re-executed only when their source changes (`freeze: auto`).
- **Update the PDF CV:** replace `files/cv.pdf`.
