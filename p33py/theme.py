from plotly import io as pio, graph_objects as go


def set_default_theme():
    # print(str(pio.templates['plotly']))
    pio.templates['p33'] = go.layout.Template(
        layout=dict(
            autosize=False,
            # width=400,
            # height=400,
            margin=dict(
                autoexpand=False,
                t=0,
                l=0,
                r=44,
                b=44,
                pad=8
            ),
            title=None,
            colorway=['#04352D', '#00715E', '#56CBB8', '#56CBB8'],
            bargroupgap=0.35,
            xaxis=dict(
                visible=False,
            ),
            yaxis=dict(
                tickformat=',.0%',
                title='',
                side='right',
            ),
            legend=dict(
                orientation='h',
                title='',
                y=0,
                x=0,
            ),
        )
    )
    pio.templates['web'] = go.layout.Template(
        layout=dict(
            paper_bgcolor='rgba(255,255,255,0)',
            plot_bgcolor='rgba(255,255,255,0)',
        )
    )

    pio.templates['draft'] = go.layout.Template(
        layout_annotations=[
            dict(
                name="draft watermark",
                text="DRAFT",
                textangle=-30,
                opacity=0.1,
                font=dict(color="black", size=100),
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                showarrow=False,
            )
        ]
    )
    pio.templates.default = "p33+web"
    # pio.templates.default = "p33+draft"
