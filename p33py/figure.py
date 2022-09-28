import plotly.express as px


def figure(metric):
    print(metric.var_scope)
    fig = px.bar(metric,
                 facet_row=metric.var_scope,
                 facet_row_spacing=0.1,
                 x=metric.var_ethnic,
                 y=metric.metric_value,
                 color=metric.var_ethnic,
                 barmode='group',
                 )
    fig.update_traces(
        texttemplate='%{y:.1%}',
        textangle=90,
        width=1
    )
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(legend_title='')
    return fig
