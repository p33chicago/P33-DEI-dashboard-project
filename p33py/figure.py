import plotly.express as px


def figure(metric):
    metric['var_scope'] = metric.var_scope.str \
        .replace('city_chi', 'Chicago') \
        .replace('state_il', 'Illinois') \
        .replace('usa', 'USA')

    fig = px.bar(metric,
                 x=metric.metric_value,
                 y=metric.var_scope,
                 color=metric.var_ethnic,
                 barmode='group',
                 orientation='h',
                 )
    fig.update_traces(
        texttemplate='%{x:.1%}',
        hovertemplate="x: %{x}<br />"
                      "y: %{y}<br />"
                      "fullData: %{fullData}<br />"
                      "data: %{data.x}<br />"
                      "text: %{text}",
    )
    fig.update_yaxes(title='')
    fig.update_xaxes(title='')
    fig.update_layout(legend_title='')

    # Place gray box behind USA
    if len(metric.var_scope.unique()) > 1:
        fig.update_layout(height=200*1.75)
        ymax = metric.metric_value.max()
        fig.add_shape(type="rect",
                      layer='below',
                      line=dict(width=0),
                      xref='x',
                      x0=0, y0=-0.5, x1=ymax * 1.1, y1=0.5,
                      fillcolor="LightGray"
                      )

    return fig
