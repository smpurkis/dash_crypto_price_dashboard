from config import app, Output, Input, html, dcc, dbc


def make_home_page() -> html.Div:
    layout = html.Div(
        [
            html.H1("Home"),
        ]
    )
    return layout
