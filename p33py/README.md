# Tech Equity Index Python code

This is a Python package for generating scorecard data and visualizations. It's intended to be used as a [package](https://docs.python.org/3/tutorial/modules.html#packages).

Example:

```python
from p33py.data.k8.noInt import calculate
from p33py.figures import vertical_bars

data = calculate()
fig = vertical_bars(data)
display(fig)
```


## Key files and folders

* [../build.py](../build.py) - main entrypoint from the build pipeline
* [data/](./data/) - functions for generating dataframes for equity indices and metrics
* [data/index.py](./data/index.py) - dataframe to help find metrics; use: `from p33py.data.index import index`
* [data/scorecard.py](./data/scorecard.py) - dataframes for things that appear on the scorecard like life stage EI's and indicator EI's for each life stage
* [figures.py](./figures.py) - functions for generating Plotly figures
* [output](./output.py) - functions for writing things to the filesystem
* [theme](./theme.py) - look-and-feel configuration for visualizations
* [equity_indices.py](./equity_indices.py) - intermediate functions used to compute EI's
* [metrics.py](./metrics.py) - intermediate functions used to compute metrics


## Build process

This is roughly what happens when the pipeline runs:

1. [../build.py](../build.py) is invoked
2. [p33py.df](./df.py) loads things from [../data/](../data/)
3. [p33py.data.scorecard](./data/scorecard.py) calculates EI dataframes
4. [p33py.figures](./figures.py) create Plotly figures for lifestage EI's
5. [p33py.output](./output.py) writes EI data (JSON) and figures (SVG and Plotly JSON) to ../output/
6. Steps 4 and 5 run for each file in ./data/{lifestage}/{metric}.py
