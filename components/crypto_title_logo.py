from dash import html


def make_title_logo(crypto_info: dict) -> html.Span:
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
