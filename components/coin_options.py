from typing import List

from Crypto import cc
from config import html, dcc


def make_coin_options(title: str, default_values: List[str]) -> html.Div:
    coins_data = cc.get_coins().to_dict("records")
    coin_options = [{"label": c["name"], "value": c["id"]} for c in coins_data]
    layout = html.Div([
        dcc.Dropdown(
            id=f'{title}-coin-options',
            options=coin_options,
            value=default_values,
            multi=True
        )
    ])
    return layout
