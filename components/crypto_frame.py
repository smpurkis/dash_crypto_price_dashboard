import re
from typing import Any, Dict

import regex

from config import html, dcc, dbc


def filter_html_tags(text: str) -> str:
    """
    Removes html tags from a string using regex
    :param text:
    :return:
    """
    return regex.sub(r"<[^>]*>", "", text)


def convert_html_to_dash_components(html_string: str) -> html.Div:
    """
    Converts a html string to dash components
    :param html_string:
    :return:
    """
    splits = re.split(
        r"(<[^>]*>(?:\w+)(?:\W+)?(?:\w+)?(?:\W+)?(?:\w+)?(?:\W+)?(?:\w+)?(?:\W+)?(?:\w+)?(?:\W+)?(?:\w+)?(?:\W+)?(?:\w+)?<\/\w+>)",
        html_string,
    )  # split on html tags correctly
    dash_converted_html = []
    for split in splits:
        if "<" in split:
            href_link = re.search(r"href=\"(.*?)\"", split)
            content = re.search(r"<[^>]*>(.*?)<\/\w+>", split)
            if content and href_link:
                content = content.group(1)
                href_link = href_link.group(1)
                dash_converted_html.append(
                    html.A(children=content, href=href_link, target="_blank")
                )
            elif content and not href_link:
                content = content.group(1)
                dash_converted_html.append(html.Span(children=content))
            elif not content and not href_link:
                dash_converted_html.append(html.Span(children=split))
        else:
            dash_converted_html.append(html.Span(children=split))
    return html.Div(children=dash_converted_html)


def make_graph(
    _id: str, crypto: str, crypto_info: Dict[str, Any], graph_fig
) -> html.Div:
    description = crypto_info["description"]["en"]
    description_components = convert_html_to_dash_components(html_string=description)
    layout = html.Div(
        id=f"{crypto}-show-div",
        children=[
            html.Span(
                style={"display": "flex", "flex-direction": "horizontal"},
                children=[
                    html.H1(
                        children=crypto_info["name"], style={"margin-right": "5px"}
                    ),
                    html.A(
                        children=html.Img(src=crypto_info["image"]["small"]),
                        href=crypto_info["links"]["homepage"][0],
                        target="_blank",
                    ),
                ],
            ),
            dbc.Button(
                children="Show Description",
                color="link",
                id={"type": "show-hide-crypto-button", "index": crypto},
            ),
            html.Div(
                id={"type": "show-hide-crypto-description", "index": crypto},
                style={"display": "none"},
                children=[
                    html.P(
                        children=description_components, style={"font-size": "1.2em"}
                    )
                ],
            ),
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
            ),
        ],
    )
    return layout
