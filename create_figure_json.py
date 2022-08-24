import pandas
import plotly.express as px
import plotly

def create_figure():
    df = pandas.read_parquet('data/parametric.parquet')
    uni = df.loc[df['Demographic'] == 'usa universities enrollment (ipeds)']
    fig = px.bar(uni.filter(items=['var_yr', 'var_value'], axis=1))
    plotly.io.write_json(fig, 'data/figure.json')
    return fig


if __name__ == "__main__":
    create_figure()

# visualizations = VisualizationCollection()

# hispanic_k8_sat_scores = Visualization()
# hispanic_k8_sat_scores.set_data_frame(df.loc[df['Demographic'] == 'usa universities enrollment (ipeds)'])
# hispanic_k8_sat_scores.create_figure = lambda df: px.bar(df, axis=1)

# visualizations.append(hispanic_k8_sat_scores)
# visualizations.save_as_json()