import pandas
import plotly.express as px
import plotly
from os.path import normpath,dirname

data_dir = normpath(f'{dirname(__file__)}/../data/')
parquet_path = f'{data_dir}/parametric.parquet'
json_path = f'{data_dir}/figure.json'

def create_figure():
    df = pandas.read_parquet(parquet_path)
    uni = df.loc[df['Demographic'] == 'usa universities enrollment (ipeds)']
    fig = px.bar(uni.filter(items=['var_yr', 'var_value'], axis=1))
    plotly.io.write_json(fig, json_path)
    print(f'wrote {json_path}')
    return fig


if __name__ == "__main__":
    create_figure()