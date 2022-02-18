from functools import cache

import pandas as pd
from pycoingecko import CoinGeckoAPI
import datetime


class CryptoCurrencies:
    cg = CoinGeckoAPI()

    @cache
    def get_coin(self, coin_id: str) -> dict:
        """
        Returns the coin information for a given coin id.
        :param coin_id:
        :return:
        """
        return self.cg.get_coin_by_id(
            coin_id,
            localization=False,
            tickers=False,
            market_data=False,
            community_data=True,
            developer_data=False,
            sparkline=False,
        )

    @cache
    def get_coins_list(self):
        return self.cg.get_coins_list()

    @cache
    def get_coins(self):
        df = pd.DataFrame(self.cg.get_coins())
        return df

    @cache
    def get_coin_options(self):
        coins_data = self.get_coins().to_dict("records")
        coin_options = [{"label": c["name"], "value": c["id"]} for c in coins_data]
        return coin_options

    @cache
    def coin_information(self):
        return self.get_coins().to_dict("records")

    @cache
    def get_all_crypto_market_data(
        self, crypto_currency: str, vs_currency: str = "usd", days: int = 10_000
    ):
        return self.cg.get_coin_market_chart_by_id(
            crypto_currency, vs_currency=vs_currency, days=days
        )

    @cache
    def get_crypto_market_data(
        self, crypto_currency: str, date_range: int = 10_000
    ) -> pd.DataFrame:
        """
        Returns the market data for a given crypto currency.
        :param crypto_currency:
        :param date_range:
        :return:
        """
        crypto_market_data = self.get_all_crypto_market_data(
            crypto_currency, vs_currency="usd", days=30 if date_range <= 30 else 10_000
        )
        df = pd.DataFrame(crypto_market_data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"] // 1000, unit="s")
        df = df[
            df["timestamp"]
            > datetime.datetime.now() - datetime.timedelta(days=date_range)
        ]
        return df


cc = CryptoCurrencies()
