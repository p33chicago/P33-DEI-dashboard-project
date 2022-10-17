[![open in Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/p33chicago/P33-DEI-dashboard-project)
[![Build](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build-and-deploy.yml/badge.svg)](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build-and-deploy.yml)


# Tech Equity Index

A website to analyze the equality - or lack thereof - that exists among underrepresented communities in the tech sector.

Features of the website:

* 📱🖥 Cross-platform: mobile-first, responsive design
* 🏎⚡️ Fast: served from edge CDN, statically rendering for server, inlined assets, client-side rendering after initial page view, only one large-ish JavaScript file, Plotly.js. ([audit])
* 🔍🧏 Accessible: can be used without JavaScript, keyboard navigation, high-contrast
* 👩‍💻 Developer-friendly: [click here to open editor in browser], [technical documentation](./docs/tech-overview.md), intuitive design system (Tailwind), [commit hooks](./githooks/INSTALLATION.md), web component and accessibility tools enabled out-of-the-box.


This repository consists of two sub repositories:

* [p33py](./p33py/): Python package for processing data to generate visualizations and JSON
* [web](./web/): website which takes visualizations and JSON as input and outputs the website as static HTML.

See [p33py/README.md](./p33py/README.md) and [web/README.md](./web/README.md) for details.


## Getting started

There are two ways of getting a development environment:

1. Using the cloud-based development workspace, Gitpod (recommended)
2. Installing things to your local machine (for advanced users)

See the sections below for more info on development environemnts, and [Tech overview](./docs/tech-overview.md) for an overview of the project.


## Cloud-based development environment (Gitpod)

To launch the development workspace in your browser, visit the project's Github page and click the "Contribute with Gitpod" badge at the top of this README.md file.

> Tip: browser keyboard shortcuts can interfere with VSCode's shortcuts. To avoid this, launch the workspace as its own application window. In Chrome, [create a shortcut] via Menu > More Tools > Create Shortcut ...


## Local development environment

⚠️ CAUTION ⚠️:️ If you use this approach, please be sure you have the proper safetynets - install the [githooks](./githooks/)!.

It's not practical to document everything needed for local development. As an alternative, you can clone the git repo, then look at .gitpod.yml to see what Gitpod does to create a workspace. See [Gitpod's documentation] for details.

Regardless, here are some important points:

* Install githooks
* If a pre-commit hook fails, understand why (there's a reason)
* Use [install.sh](./scripts/install.sh) and [start_dev.sh](./scripts/start_dev.sh) :)


## Previewing changes to scorecard and metrics

Follow these steps to test changes in a development environment:

* Make your changes in [p33py](./p33py/) or [data](./data/)
* Run [`./scripts/rebuild.sh`](./scripts/rebuild.sh)


## Notable folders

* [p33py](./p33py/) - Python codebase
* [web](./web/) - web codebase
* [notebooks](./notebooks/) - Jupyter notebooks
* [data](./data/) - raw data used as input to Python code
* [.github](./.github/) - pipeline
* [githooks](./githooks/) - commit hooks


## Additional documentation

See [docs](./docs/) for additional documentation, including:

* [Glossary](./docs/glossary.md)
* [Tech overview](./docs/tech-overview.md)
* [Accessibility](./docs/accessibility.md)


[audit]: https://web.dev/measure/?url=https%3A%2F%2Ftechequityindex.com
[click here to open editor in browser]: https://gitpod.io/#https://github.com/p33chicago/P33-DEI-dashboard-project
[Plotly for Python]: https://plotly.com/python/
[Plotly.js]: https://plotly.com/javascript/
[Jupyter]: https://jupyter.org/
[SvelteKit]: https://kit.svelte.dev/
[TailwindCSS]: https://tailwindcss.com/
[Svelte inspector]: https://joyofcode.xyz/svelte-inspector
[Tota11y]: https://khan.github.io/tota11y/
[Playwright]: https://playwright.dev/
[Gitpod]: https://gitpod.io/
[Github Pages]: https://pages.github.com/
[Github Actions]: https://github.com/features/actions
[Cloudflare]: https://www.cloudflare.com/
[pre-commit]: https://pre-commit.com/
[Black]: https://github.com/psf/black
[Prettier]: https://prettier.io/
[eslint]: https://eslint.org/
[Plotly JSON]: https://plotly.com/chart-studio-help/json-chart-schema/
[create a shortcut]: https://support.google.com/chrome_webstore/answer/3060053
[Gitpod's documentation]: https://www.gitpod.io/docs/introduction/learn-gitpod/gitpod-yaml
