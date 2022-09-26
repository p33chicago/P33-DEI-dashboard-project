import importlib
import os
from typing import Literal

from plotly import io as pio

from p33py.data.index import index
from p33py.figure import figure
from p33py.table import table

_output_dir = '../output'


def _each_datum(subdir: str, format: str):
    for i, data_from_index in index.iterrows():
        module = importlib.import_module(data_from_index.module)
        datum = module.calculate()
        dir = os.path.abspath(f'{_output_dir}/{subdir}/{data_from_index.lifestage}')
        path = f'{dir}/{data_from_index.datum_name}.{format}'
        yield datum, dir, path


def _mkdirs(dir):
    try:
        os.makedirs(dir)
    except FileExistsError:
        pass


def output_dir(dir):
    global _output_dir
    _output_dir = dir


Format = Literal['json', 'html', 'svg', 'png', 'jpg']


def figures(format: Format = 'json'):
    for datum, dir, path in _each_datum('figures', format):
        _mkdirs(dir)

        fig = figure(datum)
        if format == 'json':
            pio.write_json(fig, path)
        elif format == 'html':
            pio.write_html(fig, path, include_plotlyjs=False, full_html=False)
        elif format in ['svg', 'png', 'jpg']:
            pio.write_image(fig, path)
        print(f'Wrote {path}')
        # import sys
        # sys.exit()


def tables():
    for datum, dir, path in _each_datum('tables', 'json'):
        _mkdirs(dir)

        t = table(datum)
        with open(path, 'w') as f:
            t.to_json(f)
        print(f'Wrote {path}')


if __name__ == '__main__':
    output_dir('../output')
    figures(format='json')
    figures(format='svg')
    tables()
