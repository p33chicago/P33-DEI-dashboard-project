# Scientific notebooks

This folder contains Jupyter Lab notebooks for playing around with transformations and visualizations.

## Autoreload

When working with a Jupyter notebook that imports an external Python module, the notebook does not incorporate changes made to external modules. You can:

* Use [%autoreload magic](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) (see [caveats](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#caveats))
* Restart the notebook
* Use Python's [importlib.reload function](https://docs.python.org/3/library/importlib.html#importlib.reload)
