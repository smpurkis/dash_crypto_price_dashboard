import datetime as dt

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
        {"timestamp": dt.datetime.now() - dt.timedelta(days=1), "period": "1d"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=7), "period": "1w"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=30), "period": "1m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=90), "period": "3m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=180), "period": "6m"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=365), "period": "1y"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=730), "period": "2y"},
        {"timestamp": dt.datetime.now() - dt.timedelta(days=1825), "period": "5y"},
    ]

    # get the price data for each date range from price_data
    for date_range in date_ranges:
        date_range["price"] = float(
            price_data.loc[
                price_data["timestamp"]
                >= date_range["timestamp"] - dt.timedelta(days=1)
            ]
            .head(1)["price"]
            .values[0]
        )

    layout = html.Div("hello")

    return layout