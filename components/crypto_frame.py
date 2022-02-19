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


def on_same_line(components: list, opposite_ends: bool = False) -> html.Div:
    line = html.Div(
        children=components,
        style={
            "display": "flex",
            "flex-direction": "row",
            "justify-content": "space-between" if opposite_ends else "flex-start",
        },
    )
    return line


def make_crypto_price_frame(_id: str, crypto: str, date_range: int) -> html.Div:
    layout = html.Div(
        id=f"{crypto}-show-div",
        children=[
            on_same_line(
                components=[
                    make_title_logo(crypto=crypto),
                    make_price_summary(crypto=crypto),
                ],
                opposite_ends=True,
            ),
            make_description(crypto=crypto),
            make_price_graph(_id=_id, crypto=crypto, date_range=date_range),
            html.Hr(),
        ],
    )
    return layout
