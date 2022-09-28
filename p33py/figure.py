import plotly.express as px


def figure(metric):
    fig = px.bar(metric,
                 x=metric.var_scope,
                 y=metric.metric_value,
                 color=metric.var_ethnic,
                 barmode='group',
                 )
    fig.update_traces(
        texttemplate='%{y:.1%}',
        textangle=90,
    )
    fig.update_yaxes(title='')
    # fig.update_xaxes(range=list([0, 5]))
    fig.update_layout(legend_title='')
    return fig
