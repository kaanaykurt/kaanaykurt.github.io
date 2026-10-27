# kaanaykurt.me

Source of my personal website, built with [Quarto](https://quarto.org) and
served by GitHub Pages from `docs/`.

**Build:** open the folder in VS Code and choose *Reopen in Container*, or run

    docker build -t website-dev -f .devcontainer/Dockerfile . && docker run --rm -v "$PWD:/workspaces/website" website-dev quarto render

then commit `docs/` and push.

Content © Kaan Aykurt, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
