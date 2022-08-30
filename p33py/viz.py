import plotly.graph_objects as go
import plotly.io as pio

def set_default_theme():
    # print(str(pio.templates['plotly']))
    pio.templates['p33'] = go.layout.Template(
        layout=dict(
            title=None,
            showlegend=False,
            colorway=['#0db296', '#1d59b8', '#981717', '#ff7213', '#ffa913'],
            bargroupgap=0.025,
            # bar_textinfo=['label', 'value']
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
    pio.templates.default = "p33+draft"