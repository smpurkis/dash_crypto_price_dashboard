from Crypto import cc
from components.coin_options import make_coin_options
from components.price_graph import make_graph
from components.standard_date_options import make_standard_date_options
from config import html, dcc, date, timedelta


def make_prices_page() -> html.Div:
    _id = "prices"

    coin_options = cc.get_coin_options()
    default_values = ['bitcoin', 'ethereum']
    allowed_values = ['bitcoin', 'ethereum']
    potential_graphs = [
        make_graph(coin["value"], coin["value"], show=True if coin["value"] in ['bitcoin', 'ethereum'] else False) for
        coin in coin_options
        # if coin["value"] in allowed_values
    ]

    layout = html.Div(
        [
            html.H1("Prices"),
            make_coin_options(_id=_id, default_values=default_values),
            html.Br(),
            html.Div(style={"display": "flex"}, children=[
                dcc.DatePickerRange(
                    id=f'prices-datetime-range-picker',
                    min_date_allowed=date(2009, 1, 1),
                    max_date_allowed=date.today(),
                    initial_visible_month=date.today() - timedelta(days=7),
                    start_date=date.today() - timedelta(days=7),
                    end_date=date.today()
                ),
                make_standard_date_options(_id=_id),
            ]),
            html.Div(id=f"{_id}-graphs", children=potential_graphs),
            # make_graph(title="ravencoin", crypto="ravencoin"),
        ]
    )

    return layout
