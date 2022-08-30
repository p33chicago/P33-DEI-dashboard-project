[![Build](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build.yml/badge.svg)](https://github.com/p33chicago/P33-DEI-dashboard-project/actions/workflows/build.yml)

# P33 Chicago equity dashboard

This project helps evaluate the equality that exists among underrepresented communities in the tech sector. This is implemented by generating visualizations and compiling these visualizations into a website:

> Jupyter notebooks ≫ Plotly figure JSON ≫ Web framework ≫ Static HTML, JS, and CSS

## Using the cloud workspace (Gitpod)

To launch the development workspace in your browser, including Jupyter Lab UI, visit: [gitpod](https://gitpod.io/#https://github.com/p33chicago/P33-DEI-dashboard-project).

## Accessing data science notebooks and website dev server

See [Using Gitpod](./docs/using%20gitpod.md).

## Design guidelines

See [Design guidelines](./docs/design%20guidelines.md).

## Folder structure

* data/ - all data files go here (XSLT, CSV, etc.)
* web/ - website
* docs/ - files for humans alone (no 💻🤖 allowed); technical documentation, slide decks, design guidelines, mockups, etc.
* notebooks/ - data science notebooks for experimentation and visualization work; none of the code here is used in the pipeline or makes it way to the site; however, it does import things from the python module, p33 (see next folder below).
* p33/ - Python [package](https://docs.python.org/3/tutorial/modules.html#packages) for all of our novel code; import via `import p33`
  * \_\_init__.py - enables `from p33 import transformation`
  * ingest/ - mostly unused for now
  * transform/ - transform.r (from ingest.r); John to convert to Python?; if multiple output files, should have one file per output?
  * viz/ - visualization modules
    * figures.py - API for finding figures
    * figures/ - one file per figure; John to create example starting from create_figure_json.py


## Autoreload

When working with a Jupyter notebook that imports an external Python module, the notebook does not incorporate changes made to external modules. You can:

* Use [%autoreload magic](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) (see [caveats](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#caveats))
* Restart the notebook
* Use Python's [importlib.reload function](https://docs.python.org/3/library/importlib.html#importlib.reload)

## Data ingestion

See [Accessing data](./docs/accessing%20data.ipynb).
