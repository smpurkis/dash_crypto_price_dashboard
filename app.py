from typing import List

from components.price_graph import make_graph
from config import app
from layout import make_layout
from config import app, Output, Input, html, dcc, dbc, callback
from pages.home import make_home_page
from pages.prices import make_prices_page


if __name__ == '__main__':
    app.layout = make_layout()
    app.run_server(debug=True)