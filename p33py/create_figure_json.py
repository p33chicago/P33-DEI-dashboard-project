from viz import set_default_theme
from figures import *
import plotly.io as pio
import os

data_dir=os.path.normpath(f'{os.path.dirname(__file__)}/../data/')
json_path = f'{data_dir}/figure.json'

set_default_theme()
fig = apcs_score5.figure()
# display(fig)
pio.write_json(fig, json_path)
print(f'Wrote {json_path}')