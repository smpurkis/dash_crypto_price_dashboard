from config import html, dbc


def make_standard_date_options(_id: str):
    layout = html.Div([
        dbc.ButtonGroup(id=f"{_id}-date-options", children=[
            dbc.Button("Today", id=f"{_id}-date-options-today", color="secondary"),
            dbc.Button("1 Week", id=f"{_id}-date-options-last-week", color="primary"),
            dbc.Button("1 Month", id=f"{_id}-date-options-last-month", color="secondary"),
            dbc.Button("6 Months", id=f"{_id}-date-options-last-6-months", color="secondary"),
            dbc.Button("1 Year", id=f"{_id}-date-options-last-year", color="secondary"),
            dbc.Button("5 Years", id=f"{_id}-date-options-last-5-years", color="secondary"),
            dbc.Button("All", id=f"{_id}-date-options-last-all", color="secondary"),
        ], size="lg", style={"margin-left": "5px"}),
    ])
    return layout
