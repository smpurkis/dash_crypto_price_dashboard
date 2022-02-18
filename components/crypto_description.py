from config import html, dbc


def make_description(crypto: str, description_components: list) -> html.Div:
    layout = html.Div(
        children=[
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
        ]
    )
    return layout
