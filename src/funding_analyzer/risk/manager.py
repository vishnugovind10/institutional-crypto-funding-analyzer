import numpy as np

class RiskManager:
    def __init__(self, max_var=0.02, max_position=0.10):
        self.max_var = max_var
        self.max_position = max_position

    def calculate_position_size(self, signal_strength, volatility):
        if volatility == 0:
            return 0
        kelly_fraction = min(0.6 * 0.012 / 0.01, self.max_position)
        return kelly_fraction * abs(signal_strength)

    def calculate_var(self, returns):
        return np.percentile(returns, 5) if len(returns) >= 30 else 0.0