import numpy as np

def calculate_cvar(returns, confidence_level=0.95):
    sorted_returns = np.sort(returns)
    var = np.percentile(sorted_returns, (1 - confidence_level) * 100)
    return np.mean(sorted_returns[sorted_returns <= var]) if len(sorted_returns) > 0 else 0.0
