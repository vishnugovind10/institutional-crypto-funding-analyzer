import pandas as pd
import numpy as np

class PerformanceAnalyzer:
    def generate_performance_report(self, returns):
        cumulative = returns.cumsum()
        return {
            'sharpe_ratio': (returns.mean() / returns.std()) * np.sqrt(365 * 3) if returns.std() != 0 else 0,
            'max_drawdown': (cumulative.cummax() - cumulative).max() if len(cumulative) > 0 else 0
        }