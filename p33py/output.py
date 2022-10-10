import importlib
import os
from os.path import abspath
from shutil import rmtree
from typing import Literal

from plotly import io as pio

from p33py.data.index import index
from p33py.data.scorecard import EI_indicators_CHI, EI_lifestages_CHI
from p33py.figures import vertical_bars, horizontal_bar

_output_dir = abspath("../output")


def _each_datum(subdir: str):
    """Generator for iterating over every datum/metric"""
    for i, data_from_index in index.iterrows():
        module = importlib.import_module(data_from_index.module)
        datum = module.calculate()
        directory = f"{_output_dir}/{subdir}/{data_from_index.lifestage}"
        json_path = f"{directory}/{data_from_index.datum_name}.json"
        svg_path = f"{directory}/{data_from_index.datum_name}.svg"
        yield datum, directory, json_path, svg_path


def _makedirs_ignore_exists(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass


def make_clean_output_directory():
    """Removes and recreates output directory"""
    rmtree(_output_dir, ignore_errors=True)
    _makedirs_ignore_exists(_output_dir)


def output_dir(directory):
    """Changes where output is placed to `dir`"""
    global _output_dir
    _output_dir = abspath(directory)


Format = Literal["json", "html", "svg", "png", "jpg"]


def _lifestage_for_web(p33py_lifestage):
    if p33py_lifestage == "col":
        return "college"
    if p33py_lifestage == "emp":
        return "career"
    return p33py_lifestage


def metrics():
    """Writes all metrics as JSON and SVGs"""
    for datum, directory, json_path, svg_path in _each_datum("metrics"):
        _makedirs_ignore_exists(directory)
        fig = vertical_bars(datum)
        pio.write_json(fig, json_path)
        print(f"Wrote {json_path}")
        pio.write_image(fig, svg_path)
        print(f"Wrote {svg_path}")


def scorecard():
    """Writes lifestage JSON and figures as well as indicator Equity Indices."""
    scorecard_path = f"{_output_dir}/scorecard"
    _makedirs_ignore_exists(scorecard_path)

    # Lifestage EI JSON
    EI_stages_path = f"{scorecard_path}/lifestages.json"
    EI_lifestages_CHI["stage"] = EI_lifestages_CHI["stage"].map(_lifestage_for_web)
    EI_lifestages_CHI.to_json(EI_stages_path, orient="records")
    print(EI_lifestages_CHI)
    print(f"Wrote {EI_stages_path}")

    # Lifestage EI figures
    for lifestage_name in EI_lifestages_CHI["stage"]:
        lifestage = EI_lifestages_CHI[
            EI_lifestages_CHI["stage"] == lifestage_name
        ].copy()
        lifestage["area"] = "Chicago"
        lifestage_fig = horizontal_bar(lifestage)

        image_path = f"{scorecard_path}/figure_{_lifestage_for_web(lifestage_name)}.svg"
        lifestage_fig.write_image(format="svg", file=image_path)
        print(f"Wrote {image_path}")

        json_path = f"{scorecard_path}/figure_{_lifestage_for_web(lifestage_name)}.json"
        pio.write_json(lifestage_fig, file=json_path)
        print(f"Wrote {json_path}")

    # Indicator JSON
    EI_indicators_path = f"{scorecard_path}/indicators.json"
    EI_indicators_CHI["stage"] = EI_indicators_CHI["stage"].map(_lifestage_for_web)
    EI_indicators_CHI.to_json(EI_indicators_path, orient="records")
    print(f"Wrote {EI_indicators_path}")
