import re
from typing import Any, Dict

import plotly.graph_objects as go
import regex

from components.crypto_description import make_description
from components.crypto_price_summary import make_price_summary
from components.crypto_title_logo import make_title_logo
from components.price_graph import make_price_graph
from config import html


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


def on_same_line(components: list) -> html.Div:
    line = html.Div(
        children=components,
        style={"display": "flex", "flex-direction": "row"},
    )
    return line


def make_crypto_price_frame(
    _id: str, crypto: str, crypto_info: Dict[str, Any], graph_fig: go.Figure
) -> html.Div:
    description = crypto_info["description"]["en"]
    description_components = convert_html_to_dash_components(html_string=description)
    layout = html.Div(
        id=f"{crypto}-show-div",
        children=[
            on_same_line(
                components=[
                    make_title_logo(crypto_info=crypto_info),
                    make_price_summary(crypto_info=crypto_info),
                ]
            ),
            make_description(
                crypto=crypto, description_components=description_components
            ),
            make_price_graph(_id=_id, crypto=crypto, graph_fig=graph_fig),
        ],
    )
    return layout
