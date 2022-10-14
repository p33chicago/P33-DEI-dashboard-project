import plotly.express as px


def vertical_bars(metric):
    metric["var_scope"] = (
        metric.var_scope.str.replace("city_chi", "Chicago")
        .replace("state_il", "Illinois")
        .replace("usa", "USA")
    )
    metric["var_ethnic"] = metric.var_ethnic.str.capitalize()

    fig = px.bar(
        metric,
        x=metric.var_scope,
        y=metric.metric_value,
        color=metric.var_ethnic,
        barmode="group",
        width=365,
        height=200,
        color_discrete_sequence=["#04352D", "#00715E", "#56CBB8", "#76EBD8"],
    )
    fig.update_traces(
        texttemplate="%{y:.1%}",
        textangle=90,
        hovertemplate="%{data.name}: %{y:.2%} (%{x})<extra></extra>",
    )
    fig.update_yaxes(title="", tickformat=",.0%", side="right", fixedrange=True)
    fig.update_xaxes(title="", side="top")
    fig.update_layout(legend_title="", margin=dict(t=30, l=0, r=40, b=54, pad=8))

    # Place gray box behind USA
    if len(metric.var_scope.unique()) > 1:
        ymax = metric.metric_value.max()
        fig.add_shape(
            type="rect",
            layer="below",
            line=dict(width=0),
            xref="x",
            x0=0.5,
            y0=0,
            x1=1.5,
            y1=ymax,
            fillcolor="LightGray",
        )

    return fig


def horizontal_bar(metric):
    fig = px.bar(
        metric,
        x="weighted_EI_stage",
        y="var_scope",
        color="var_scope",
        orientation="h",
        range_x=[0, 100],
        width=268,
        height=113,
        color_discrete_sequence=["#00715e","blue"],
    )
    fig.update_yaxes(title="", side="left")
    fig.update_xaxes(title="", side="bottom", tickvals=list(range(0, 101, 25)))
    fig.update_layout(
        legend_title="",
        margin=dict(t=0, l=57, r=12, b=37, pad=8),
    )
    fig.update_traces(
        hovertemplate="%{x:.3}<extra></extra>",
        showlegend=False
    )
    return fig
