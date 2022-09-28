import plotly.express as px


def figure(metric):
    metric['var_scope'] = metric.var_scope.str\
        .replace('city_chi', 'Chicago')\
        .replace('state_il', 'Illinois')\
        .replace('usa', 'USA')

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
    fig.update_xaxes(title='')
    fig.update_layout(legend_title='')

    # Place gray box behind USA
    if len(metric.var_scope.unique()) > 1:
        fig.add_shape(type="rect",
                      layer='below',
                      line=dict(width=0),
                      xref='x',
                      x0=0.5, y0=0, x1=1.5, y1=1,
                      fillcolor="LightGray"
                      )

    return fig
