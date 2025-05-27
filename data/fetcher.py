import ccxt.pro as ccxt
import pandas as pd

async def fetch_funding_rates(exchange, symbols):
    data = []
    for symbol in symbols:
        rates = await exchange.fetch_funding_rate_history(symbol, limit=100)
        data.extend([{
            'timestamp': pd.to_datetime(r['timestamp'], unit='ms'),
            'exchange': exchange.id,
            'symbol': symbol,
            'funding_rate': r['fundingRate']
        } for r in rates])
    return pd.DataFrame(data)
