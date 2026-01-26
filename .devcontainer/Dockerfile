FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /workspaces/website

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates curl git openssh-client \
  fontconfig \
  fonts-linuxlibertine \
  texlive-xetex \
  texlive-latex-base \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-science \
  texlive-plain-generic \
  latexmk \
  libfreetype6 \
  libpng16-16 \
  cm-super dvipng dvisvgm ghostscript \
  && rm -rf /var/lib/apt/lists/* \
  && fc-cache -f -v

# Install Quarto
ARG QUARTO_VERSION=1.8.27
ARG ARCH=arm64 

RUN curl -fsSL https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-${ARCH}.deb \
    -o /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml ./
RUN uv sync
