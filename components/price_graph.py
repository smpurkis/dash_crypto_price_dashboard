import re
from typing import Any, Dict

import regex

from config import html, dcc


def filter_html_tags(text: str) -> str:
    """
    Removes html tags from a string using regex
    :param text:
    :return:
    """
    return regex.sub(r'<[^>]*>', '', text)

def convert_html_to_dash_components(html_string: str) -> html.Div:
    """
    Converts a html string to dash components
    :param html_string:
    :return:
    """
    splits = re.split(r"(<[^>]*>)", html_string)  # split on html tags correctly
    components = html.Div()


def make_graph(_id: str, crypto: str, crypto_info: Dict[str, Any], graph_fig) -> html.Div:
    # description = filter_html_tags(text="\n".join(crypto_info['description']['en'].split("\r\n\r\n")))
    description = crypto_info['description']['en']
    description_components = convert_html_to_dash_components(html_string=description)
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
            html.P(children=description, style={"font-size": "1.2em"}),
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
