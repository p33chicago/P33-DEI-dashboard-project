import os
import pandas as pd
import plotly.express as px
import numpy as np

def figure():
    data_dir=os.path.normpath(f'{os.path.dirname(__file__)}/../../data/')
    # data_dir=os.path.normpath(f'{os.getcwd()}/../data/')
    df = pd.read_csv(f'{data_dir}/df_DEI_tidy_final.csv')
    df['var_ethnic'] = df.var_ethnic.str.lower()
    df = df[df.var_ethnic.isin(['hispanic', 'black', 'asian', 'white'])]
    df = df[df.var_yr == 2021]
    df = df[df.var_key == 'apcs_score5']
    df = df.sort_values(by='var_ethnic')
    df['group'] = df['var_ethnic']
    df['population'] = np.select([df.var_scope == 'usa', df.var_scope != 'usa'], [df.population / 100, df.population])
    df['area'] = np.select([df.var_scope == 'city_chi'], ['city of chicago'], default=df.var_scope)
    # display(df)
    fig = px.bar(df, x=df.area, y=df.population, color=df.group, barmode='group', text_auto=True)
    fig.update_traces(texttemplate='%{group} %{y}')
    fig.update_yaxes(title='population')
    return fig
    # fig.layout.yaxis
