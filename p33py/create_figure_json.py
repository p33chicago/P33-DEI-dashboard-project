from .viz import set_default_theme
from .figures import *
import plotly.io as pio

data_dir=os.path.normpath(f'{os.getcwd()}/../data/')
json_path = f'{data_dir}/figure.json'

fig = apcs_score5.figure()
display(fig)
pio.write_json(fig, json_path)
print(f'Wrote {json_path}')