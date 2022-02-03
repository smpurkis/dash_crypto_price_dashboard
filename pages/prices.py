from Crypto import cc
from components.coin_options import make_coin_options
from components.price_graph import make_graph
from config import html


def make_prices_page() -> html.Div:
    title = "prices"

    coin_options = cc.get_coin_options()
    default_values = ['bitcoin', 'ethereum']
    potential_graphs = [
        make_graph(coin["value"], coin["value"], show=True if coin["value"] in ['bitcoin', 'ethereum'] else False) for
        coin in coin_options]

    layout = html.Div(
        [
            html.H1("Prices"),
            make_coin_options(title=title, default_values=default_values),
            html.Div(id=f"{title}-graphs", children=potential_graphs),
            # make_graph(title="ravencoin", crypto="ravencoin"),
        ]
    )

    # @callback(
    #     Output(f"{title}-graphs", "children"),
    #     [Input(f"{title}-coin-options", "value")]
    # )
    # def populate_graphs(coins: List[str]):
    #     graphs = []
    #     for coin in coins:
    #         graphs.append(make_graph(title=coin, crypto=coin))
    #     return graphs
    #
    # @callback(
    #     Output(f"{title}-graphs", "children"),
    #     [Input(f"{title}-coin-options", "value")]
    # )
    # def populate_graphs(coins: List[str]):
    #     graphs = []
    #     for coin in coins:
    #         graphs.append(make_graph(title=coin, crypto=coin))
    #     return graphs

    return layout
