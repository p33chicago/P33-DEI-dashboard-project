from plotly import io as pio, graph_objects as go


def set_default_theme():
    # print(str(pio.templates['plotly']))
    pio.templates['p33'] = go.layout.Template(
        layout=dict(
            # autosize=False,
            width=300,
            height=200,
            margin=dict(
                t=0,
                l=0,
                r=20,
                b=0,
                pad=0
            ),
            title=None,
            colorway=['#04352D', '#00715E', '#56CBB8', '#76EBD8'],
            bargroupgap=0.125,
            xaxis=dict(
                visible=False,
            ),
            yaxis=dict(
                tickangle=90,
                side='right',
                # visible=True,
                # tickformat=',.0%',
                # title='',
                # tickangle=90,
                # fixedrange=True,
            ),
            legend=dict(
                borderwidth=0,
                # itemwidth=30,
                orientation='h',
                title='',
                x=-0.0125,
                y=0,
                # yanchor='top'
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
