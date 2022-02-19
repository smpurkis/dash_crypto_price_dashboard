from config import html


def make_home_page() -> html.Div:
    layout = html.Div(
        [
            html.H1("Home"),
            html.P("Summary datatable will be here."),
        ]
    )
    return layout
