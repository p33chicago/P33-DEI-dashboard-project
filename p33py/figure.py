import plotly.express as px


def figure(metric):
    fig = px.bar(metric,
                 x=metric.var_scope,
                 y=metric.metric_value,
                 color=metric.var_ethnic,
                 barmode='group')
    fig.update_traces(texttemplate='%{y}')
    fig.update_yaxes(title='proportion')
    return fig
