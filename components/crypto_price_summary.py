import datetime as dt

import dash_bootstrap_components as dbc
from dash import html

from Crypto import cc


def make_price_summary(crypto: str) -> html.Div:
    """
    Creates a price summary for a given crypto for periods of:
    1 day, 1 week, 1 month, 3 months, 6 months, 1 year, 2 years, 5 years
    :param crypto:
    :return:
    """
    price_data = cc.get_crypto_market_data(crypto_currency=crypto)
    date_ranges = [
        {"timestamp": dt.datetime.now(), "period": "Today"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=1), "period": "1d"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=7), "period": "1w"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=30), "period": "1m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=90), "period": "3m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=180), "period": "6m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=365), "period": "1y"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=730), "period": "2y"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=1825), "period": "5y"},
    ]

    today_price = float(price_data.iloc[-1]["price"])
    date_ranges[0]["price"] = today_price
    date_ranges[0]["percent_change"] = 0

    # get the price data for each date range from price_data
    for date_range in date_ranges[1:]:
        date_range["price"] = float(
            price_data.loc[
                price_data["timestamp"]
                >= date_range["timestamp"] - dt.timedelta(days=1)
            ]
            .head(1)["price"]
            .values[0]
        )

        date_range["percent_change"] = (
            (today_price - date_range["price"]) / date_range["price"]
        ) * 100

    date_ranges = list(reversed(date_ranges))

    table_header = [
        html.Thead(html.Tr([html.Th(p["period"]) for p in date_ranges])),
    ]

    table_body = [
        html.Tbody(
            [
                html.Tr(
                    [
                        html.Td(
                            children=f"{'+' if p['percent_change'] > 0 else ''}{p['percent_change']:.1f}% ({int(p['price'])})",
                            style={
                                "color": "red" if p["percent_change"] < 0 else "green"
                            },
                        )
                        for p in date_ranges
                    ]
                )
            ]
        )
    ]

    layout = dbc.Table(
        table_header + table_body,
        bordered=True,
        dark=True,
        hover=True,
        responsive=True,
        striped=True,
    )

    return layout
