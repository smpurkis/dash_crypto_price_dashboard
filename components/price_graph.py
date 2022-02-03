from typing import List

import plotly.graph_objects as go

from Crypto import cc
from _callbacks import _callbacks
from config import app, Output, Input, parse, html, dcc


def make_graph(title: str, crypto: str, show: bool = False) -> html.Div:
    layout = html.Div(
        id=f"{title}-show-div",
        style={"display": "none", "visibility": "hidden"} if not show else {},
        children=[
            html.H1(children=title),
            html.Div(children='''
                Dash: A web application framework for your data.
            '''),
            dcc.Loading(
                id=f"{title}-loading-1",
                children=[html.Div([dcc.Graph(id=f'{title}-example-graph')])],
                type="circle",
            ),
        ])

    def callbacks():
        @app.callback(
            [Output(f'{title}-example-graph', "figure"),
             Output(f"{title}-show-div", "style")],
            [Input(f"prices-datetime-range-picker", "start_date"),
             Input(f"prices-datetime-range-picker", "end_date"),
             Input(f"prices-coin-options", "value")]
        )
        def hydrated_graph(start_date, end_date, cryptos_to_show: List[str]):
            if title not in cryptos_to_show:
                fig = go.Figure()
                fig.add_trace(
                    go.Scatter(
                        x=[1, 2, 3],
                        y=[1, 2, 3],
                        textfont=dict(size=160, color="LightSeaGreen")
                    )
                ),
                fig.update_layout(hovermode="x")
                return fig, {"display": "none", "visibility": "hidden"}
            date_range = (parse(end_date) - parse(start_date)).days
            df = cc.get_crypto_market_data(crypto_currency=crypto, date_range=date_range)
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=df["timestamp"],
                    y=df["price"],
                    textfont=dict(size=160, color="LightSeaGreen")
                )
            ),
            fig.update_layout(hovermode="x")
            return fig, {}

    _callbacks.append(callbacks)
    return layout
