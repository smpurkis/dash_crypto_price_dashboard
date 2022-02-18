from dash import html

from Crypto import cc


def make_title_logo(crypto: str) -> html.Span:
    crypto_info = cc.get_coin(coin_id=crypto)

    layout = html.Span(
        style={"display": "flex", "flex-direction": "horizontal"},
        children=[
            html.H1(children=crypto_info["name"], style={"margin-right": "5px"}),
            html.H1(
                children=f"""({crypto_info["symbol"].upper()})""",
                style={"margin-right": "5px"},
            ),
            html.A(
                children=html.Img(src=crypto_info["image"]["small"]),
                href=crypto_info["links"]["homepage"][0],
                target="_blank",
            ),
        ],
    )
    return layout
