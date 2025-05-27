import pandas as pd

class MomentumStrategy:
    def __init__(self, lookback=10, threshold=0.01):
        self.lookback = lookback
        self.threshold = threshold

    def generate_signals(self, data):
        signals = data.copy()
        signals['momentum'] = signals['funding_rate'].rolling(self.lookback).mean()
        signals['signal'] = 0
        signals.loc[signals['momentum'] > self.threshold, 'signal'] = 1
        signals.loc[signals['momentum'] < -self.threshold, 'signal'] = -1
        return signals