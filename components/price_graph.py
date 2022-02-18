import plotly.graph_objects as go

from config import html, dcc


def make_price_graph(_id: str, crypto: str, graph_fig: go.Figure):
    layout = html.Div(
        children=[
            dcc.Loading(
                id=f"{crypto}-loading-1",
                children=[
                    html.Div(
                        [
                            dcc.Graph(
                                id={"type": f"{_id}-graph", "index": "n_clicks"},
                                figure=graph_fig,
                            )
                        ]
                    )
                ],
                type="circle",
            )
        ]
    )
    return layout
