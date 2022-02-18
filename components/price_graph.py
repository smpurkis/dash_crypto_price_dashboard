import plotly.graph_objects as go

from Crypto import cc
from config import html, dcc


def generate_graph(crypto, date_range: int) -> go.Figure:
    df = cc.get_crypto_market_data(crypto_currency=crypto, date_range=date_range)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["price"],
            textfont=dict(size=160, color="LightSeaGreen"),
        )
    ),
    fig.update_layout(hovermode="x")
    return fig


def make_price_graph(_id: str, crypto: str, date_range: int):
    graph_fig = generate_graph(crypto, date_range)

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
