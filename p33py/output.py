import importlib
import os
from os.path import abspath
from shutil import rmtree
from typing import Literal

from plotly import io as pio

from p33py.data.index import index
from p33py.data.scorecard import EI_indicators_CHI, EI_lifestages_CHI
from p33py.figures import vertical_bars
from p33py.table import table

_output_dir = abspath("../output")


def _each_datum(subdir: str, format: str):
    """Generator for iterating over every datum/metric"""
    for i, data_from_index in index.iterrows():
        module = importlib.import_module(data_from_index.module)
        datum = module.calculate()
        dir = f"{_output_dir}/{subdir}/{data_from_index.lifestage}"
        path = f"{dir}/{data_from_index.datum_name}.{format}"
        yield datum, dir, path


def _makedirs_ignore_exists(dir):
    try:
        os.makedirs(dir)
    except FileExistsError:
        pass


def make_clean_output_directory():
    """Removes and recreates output directory"""
    rmtree(_output_dir, ignore_errors=True)
    _makedirs_ignore_exists(_output_dir)


def output_dir(dir):
    """Changes where output is placed to `dir`"""
    global _output_dir
    _output_dir = abspath(dir)


Format = Literal["json", "html", "svg", "png", "jpg"]


def figures(format: Format = "json"):
    for datum, dir, path in _each_datum("figures", format):
        _makedirs_ignore_exists(dir)
        fig = vertical_bars(datum)
        if format == "json":
            pio.write_json(fig, path)
        elif format == "html":
            pio.write_html(fig, path, include_plotlyjs=False, full_html=False)
        elif format in ["svg", "png", "jpg"]:
            pio.write_image(fig, path)
        print(f"Wrote {path}")


def tables():
    for datum, dir, path in _each_datum("tables", "json"):
        _makedirs_ignore_exists(dir)
        t = table(datum)
        with open(path, "w") as f:
            t.to_json(f)
        print(f"Wrote {path}")


def equity_indices():
    destination = f"{_output_dir}/equity_indices"
    _makedirs_ignore_exists(destination)

    EI_stages_path = f"{destination}/lifestages.json"
    EI_lifestages_CHI.to_json(EI_stages_path, orient="records")
    print(f"Wrote {EI_stages_path}")

    EI_indicators_path = f"{destination}/indicators.json"
    EI_indicators_CHI.to_json(EI_indicators_path, orient="records")
    print(f"Wrote {EI_indicators_path}")
