from typing import List

from components.crypto_frame import make_graph
from config import app, Output, Input, html, dcc, dbc, callback
from pages.home import make_home_page
from pages.prices import make_prices_page
from _callbacks import _callbacks

def make_layout() -> html.Div:
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    }

    # the styles for the main content position it to the right of the sidebar and
    # add some padding.
    CONTENT_STYLE = {
        "margin-right": "2rem",
        "padding": "2rem 1rem",
        "margin-left": "18rem",

    }

    sidebar = html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P(
                "A simple sidebar layout with navigation links", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Prices", href="/prices", active="exact"),
                    dbc.NavLink("Forecast", href="/forecast", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    content = html.Div(id="page-content", style=CONTENT_STYLE)

    layout = html.Div(
        [dcc.Location(id="url"), sidebar, content],
        # style={
        #     "background-color": "#282c34",
        #     'border': 'solid 1px #A2B1C6',
        #     'border-radius': '5px',
        #     'padding': '50px',
        #     'margin-top': '20px'
        # }
    )
    pages = {
        "home": make_home_page(),
        "prices": make_prices_page(),
        # "page-2": make_page_2(),
    }

    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        if pathname == "/":
            return pages["home"]
        elif pathname == "/prices":
            return pages["prices"]
        elif pathname == "/forecast":
            return html.P("Oh cool, this is page 2!")
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )

    for callback_fns in _callbacks:
        callback_fns()
    return layout
