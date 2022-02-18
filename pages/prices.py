import dash
import plotly.graph_objects as go
from dash import MATCH

from Crypto import cc
from _callbacks import _callbacks
from components.coin_options import make_coin_options
from components.crypto_frame import make_crypto_price_frame
from components.standard_date_options import make_standard_date_options
from components.standard_date_options import preset_dates, ids_dates
from config import app, Output, Input, parse, html, dcc
from config import date, timedelta


def make_prices_page() -> html.Div:
    _id = "prices"

    coin_options = cc.get_coin_options()
    default_values = ["bitcoin", "ethereum"]

    layout = html.Div(
        [
            html.H1("Prices"),
            make_coin_options(_id=_id, default_values=default_values),
            html.Br(),
            html.Div(
                style={"display": "flex"},
                children=[
                    dcc.DatePickerRange(
                        id=f"{_id}-datetime-range-picker",
                        min_date_allowed=date(2009, 1, 1),
                        max_date_allowed=date.today(),
                        initial_visible_month=date.today() - timedelta(days=7),
                        start_date=date.today() - timedelta(days=7),
                        end_date=date.today(),
                    ),
                    make_standard_date_options(_id=_id),
                ],
            ),
            html.Div(id=f"{_id}-graphs", children=[]),
            # make_crypto_price_frame(title="ravencoin", crypto="ravencoin"),
        ]
    )

    def generate_graph(crypto, date_range: int) -> go.Figure:
        df = cc.get_crypto_market_data(crypto_currency=crypto, date_range=date_range)
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=df["timestamp"],
                y=df["price"],
                textfont=dict(size=160, color="LightSeaGreen"),
            )
        ),
        fig.update_layout(hovermode="x")
        return fig

    def callbacks():
        @app.callback(
            [
                Output(f"{_id}-graphs", "children"),
                Output(f"{_id}-datetime-range-picker", "start_date"),
                Output(f"{_id}-datetime-range-picker", "end_date"),
            ],
            [
                Input(f"{_id}-datetime-range-picker", "start_date"),
                Input(f"{_id}-datetime-range-picker", "end_date"),
                Input(f"{_id}-coin-options", "value"),
                [Input(f"{_id}{id_date}", "n_clicks") for id_date in ids_dates],
            ],
        )
        def hydrated_graph(start_date, end_date, active_cryptos, *active_date_buttons):
            ctx = dash.callback_context
            coins_information = cc.coin_information()

            triggered_button = (
                f"""-{ctx.triggered[0]["prop_id"].split(".")[0].split("-", 1)[-1]}"""
            )
            if triggered_button in ids_dates:
                index = ids_dates.index(triggered_button)
                timedelta_str = list(preset_dates.keys())[index]
                parse_timedelta = preset_dates[timedelta_str]["timedelta"]
                date_range = parse_timedelta.days
            else:
                date_range = (parse(end_date) - parse(start_date)).days

            graphs = [html.Br()]
            for crypto in active_cryptos:
                # coin_info = [coin for coin in coins_information if coin["id"] == crypto]
                coin_info = cc.get_coin(coin_id=crypto)
                if coin_info:
                    # coin_info = coin_info[0]
                    graphs.append(
                        make_crypto_price_frame(
                            _id=_id,
                            crypto=crypto,
                            crypto_info=coin_info,
                            graph_fig=generate_graph(crypto, date_range),
                        )
                    )
                else:
                    graphs.append(html.Div(f"{crypto} is not supported"))
            start_date = date.today() - timedelta(days=date_range)
            return [graphs, start_date, end_date]

        @app.callback(
            [
                Output(
                    {"type": "show-hide-crypto-description", "index": MATCH}, "style"
                ),
                Output({"type": "show-hide-crypto-button", "index": MATCH}, "children"),
            ],
            [
                Input({"type": "show-hide-crypto-button", "index": MATCH}, "n_clicks"),
                Input(
                    {"type": "show-hide-crypto-description", "index": MATCH}, "style"
                ),
            ],
        )
        def show_description(n_clicks, value):
            if n_clicks is None:
                return {"display": "none"}, "Show Description"
            else:
                return {"display": "block"} if value["display"] == "none" else {
                    "display": "none"
                }, "Hide Description" if value[
                    "display"
                ] == "none" else "Show Description"

    _callbacks.append(callbacks)
    return layout
