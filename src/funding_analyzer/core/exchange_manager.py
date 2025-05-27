import ccxt.pro as ccxt
import pandas as pd
import logging

class ExchangeManager:
    def __init__(self, exchanges, credentials):
        self.exchanges = {name: getattr(ccxt, name)({
            'apiKey': credentials.get(f"{name.upper()}_API_KEY"),
            'secret': credentials.get(f"{name.upper()}_SECRET"),
            'enableRateLimit': True
        }) for name in exchanges}

    async def fetch_funding_rates(self, symbols):
        all_data = []
        for name, exchange in self.exchanges.items():
            for symbol in symbols:
                try:
                    rates = await exchange.fetch_funding_rate_history(symbol, limit=100)
                    all_data.extend([{
                        'timestamp': pd.to_datetime(r['timestamp'], unit='ms'),
                        'exchange': name,
                        'symbol': symbol,
                        'funding_rate': r['fundingRate']
                    } for r in rates])
                    logging.info(f"Fetched rates from {name}")
                except Exception as e:
                    logging.error(f"Error fetching from {name}: {e}")
        return pd.DataFrame(all_data) if all_data else pd.read_csv('data/sample_funding_rates.csv')