from datetime import timedelta, datetime

import dash
from dash import Output, Input

from _callbacks import _callbacks
from config import app, html, dbc

preset_dates = {
    "Today": {
        "_id": "-date-options-today",
        "color": "secondary",
        "timedelta": timedelta(days=1),
    },
    "1 Week": {
        "_id": "-date-options-last-week",
        "color": "primary",
        "timedelta": timedelta(days=7),
    },
    "1 Month": {
        "_id": "-date-options-last-month",
        "color": "secondary",
        "timedelta": timedelta(days=30),
    },
    "6 Months": {
        "_id": "-date-options-last-6-months",
        "color": "secondary",
        "timedelta": timedelta(days=180),
    },
    "1 Year": {
        "_id": "-date-options-last-year",
        "color": "secondary",
        "timedelta": timedelta(days=365),
    },
    "5 Years": {
        "_id": "-date-options-last-5-years",
        "color": "secondary",
        "timedelta": timedelta(days=1825),
    },
    "All": {
        "_id": "-date-options-last-all",
        "color": "secondary",
        "timedelta": timedelta(days=(datetime.now() - datetime(2009, 1, 1)).days),
    },
}
ids_dates = [s["_id"] for s in preset_dates.values()]


def make_standard_date_options(_id: str):
    layout = html.Div(
        [
            dbc.ButtonGroup(
                id=f"{_id}-date-options",
                children=[
                    dbc.Button(
                        children=name,
                        id=f"{_id}{settings['_id']}",
                        color=settings["color"],
                    )
                    for name, settings in preset_dates.items()
                ],
                size="lg",
                style={"margin-left": "5px"},
            ),
        ]
    )

    def callbacks():
        @app.callback(
            [Output(f"{_id}{id_date}", "color") for id_date in ids_dates],
            [Input(f"{_id}{id_date}", "n_clicks") for id_date in ids_dates],
        )
        def make_primary(*n_clicks):
            ctx = dash.callback_context
            triggered_button = (
                f"""-{ctx.triggered[0]["prop_id"].split(".")[0].split("-", 1)[-1]}""" ""
            )
            colors = ["secondary" for name in preset_dates.keys()]
            if triggered_button in ids_dates:
                button_index = ids_dates.index(triggered_button)
                colors[button_index] = "primary"
            else:
                colors[1] = "primary"
            return colors

    _callbacks.append(callbacks)
    return layout
