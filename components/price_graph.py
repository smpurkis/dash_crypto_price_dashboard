from typing import Any, Dict

from config import html, dcc


def make_graph(_id: str, crypto: str, crypto_info: Dict[str, Any], graph_fig) -> html.Div:
    layout = html.Div(
        id=f"{crypto}-show-div",
        children=[
            html.Span(
                style={
                    "display": "flex",
                    "flex-direction": "horizontal"
                },
                children=[
                    html.H1(children=crypto_info["name"], style={"margin-right": "5px"}),
                    html.Img(src=crypto_info["image"]["small"]),
                ]),
            html.Div(children='''
                Dash: A web application framework for your data.
            '''),
            dcc.Loading(
                id=f"{crypto}-loading-1",
                children=[
                    html.Div([
                        dcc.Graph(
                            id={
                                "type": f"{_id}-graph",
                                "index": "n_clicks"
                            },
                            figure=graph_fig
                        )
                    ])
                ],
                type="circle",
            ),
        ])
    return layout
