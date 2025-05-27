import pandas as pd

class StatisticalArbitrage:
    def __init__(self, lookback_period=30, entry_threshold=2.0):
        self.lookback_period = lookback_period
        self.entry_threshold = entry_threshold

    def generate_signals(self, data):
        signals = data.copy()
        signals['ma'] = signals.groupby(['exchange', 'symbol'])['funding_rate'].transform(
            lambda x: x.rolling(self.lookback_period).mean()
        )
        signals['std'] = signals.groupby(['exchange', 'symbol'])['funding_rate'].transform(
            lambda x: x.rolling(self.lookback_period).std()
        )
        signals['z_score'] = (signals['funding_rate'] - signals['ma']) / signals['std']
        signals['signal'] = 0
        signals.loc[signals['z_score'] > self.entry_threshold, 'signal'] = -1
        signals.loc[signals['z_score'] < -self.entry_threshold, 'signal'] = 1
        signals.loc[abs(signals['z_score']) < 0.5, 'signal'] = 0
        return signals