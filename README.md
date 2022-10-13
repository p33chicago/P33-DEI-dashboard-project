[![Open in Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/p33chicago/P33-DEI-dashboard-project)
[![Build](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build-and-deploy.yml/badge.svg)](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build-and-deploy.yml)

# P33 Chicago equity dashboard

This project helps evaluate the equality that exists among underrepresented communities in the tech sector. This is implemented by generating visualizations and compiling these visualizations into a website:

> Python data processing ≫ Plotly figure JSON ≫ Web framework ≫ Static HTML, JS, and CSS

## Installation

There are two ways of getting a development environment:

1. Using the cloud workspace, Gitpod (recommended)
2. Installing things to your local machine

Advantages to using the cloud workspace:

* Click a link and get a fully installed, running development environment
* Everyone has the same environment - no "works on my machine" syndrome

### Using the cloud workspace (Gitpod)

To launch the development workspace in your browser, including Jupyter Lab UI, visit: [gitpod](https://gitpod.io/#https://github.com/p33chicago/P33-DEI-dashboard-project).

To learn more about accessing data science notebooks and the website dev server, see [Using Gitpod](./docs/using%20gitpod.md).

### Developing locally

Install git, Python, and nodejs, then run:

```shell
# Install git hooks, so safety measures run before pushing changes
git config --local core.hooksPath githooks

# Install
eval scripts/install.sh

# Start dev server
eval scripts/start_dev.sh
```

## Folder structure

**NOTE:** If a file/folder isn't listed below, it's for some specific development tool; you can find more info by googling the filename. e.g. [.gitpod.yml](https://google.com/search?q=.gitpod.yml).

In order of importance:

**/README.md
: Separate documentation exists in various folders.

web/
: Website source code. Has its own [README](web/README.md).

p33py/
: Python [package](https://docs.python.org/3/tutorial/modules.html#packages) for all of our novel code; import via `import p33py`

data/
: all data files go here (XSLT, CSV, etc.)

docs/
: files for humans alone (no 💻🤖 allowed); technical documentation, slide decks, design guidelines, mockups, etc.

scripts/
: Useful shell scripts

.github/
: Files for our CI/CD pipeline (Github Actions)

build.py
: Entrypoint for all our code that processes data.

.githooks/
: Files that should should run at certain times when running version control. See [githooks/INSTALLATION.md](githooks/INSTALLATION.md) for instructions. See [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) for background.

notebooks/
: data science notebooks for experimentation and visualization work; none of the code here is used in the pipeline or makes it way to the site; however, it does import things from the python module, p33 (see above).

output/
: Where build output is placed. Safe to delete, because it's recreated with every build.

## Accessibility

We want to make our website usable to as many people as we can. Our visualizations present unique challenges. See [docs/accessibility.md](docs/accessibility.md) for details.
