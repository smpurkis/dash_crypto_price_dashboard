import pandas as pd
from pycoingecko import CoinGeckoAPI
from functools import cache


class CryptoCurrencies:
    cg = CoinGeckoAPI()

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
    def get_crypto_market_data(self, crypto_currency: str, date_range: int) -> pd.DataFrame:
        """
        Returns the market data for a given crypto currency.
        :param crypto_currency:
        :param date_range:
        :return:
        """
        crypto_market_data = self.cg.get_coin_market_chart_by_id(crypto_currency, vs_currency='usd', days=date_range)
        df = pd.DataFrame(crypto_market_data['prices'], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"] // 1000, unit="s")
        return df



cc = CryptoCurrencies()
