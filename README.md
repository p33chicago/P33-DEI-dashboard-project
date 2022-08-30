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

## Autoreload

When working with a Jupyter notebook that imports an external Python module, the notebook does not incorporate changes made to external modules. You can:

* Use [%autoreload magic](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) (see [caveats](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#caveats))
* Restart the notebook
* Use Python's [importlib.reload function](https://docs.python.org/3/library/importlib.html#importlib.reload)

## Data ingestion

See [Accessing data](./docs/accessing%20data.ipynb).
