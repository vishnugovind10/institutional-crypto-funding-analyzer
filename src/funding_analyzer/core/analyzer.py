import asyncio
import logging
from .exchange_manager import ExchangeManager
from ..strategies.statistical_arb import StatisticalArbitrage
from ..risk.manager import RiskManager
from ..reporting.performance import PerformanceAnalyzer
from ..reporting.visualizations import plot_results
from ..utils.notifications import send_alert

logging.basicConfig(filename='logs/funding_analyzer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FundingAnalyzer:
    def __init__(self, exchanges, symbols, credentials):
        self.exchange_manager = ExchangeManager(exchanges, credentials)
        self.risk_manager = RiskManager()
        self.performance_analyzer = PerformanceAnalyzer()
        self.strategy = StatisticalArbitrage()
        self.symbols = symbols

    async def run(self):
        logging.info("Starting Funding Rate Analyzer")
        data = await self.exchange_manager.fetch_funding_rates(self.symbols)
        signals = self.strategy.generate_signals(data)
        returns = self.simulate_trading(signals)
        metrics = self.performance_analyzer.generate_performance_report(returns)
        plot_results(data, returns, metrics)
        send_alert("Backtest Complete", f"Sharpe: {metrics['sharpe_ratio']:.2f}")
        print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}, Max Drawdown: {metrics['max_drawdown']:.4f}")

    def simulate_trading(self, signals):
        capital = 1_000_000  # $1M initial capital
        returns = []
        for _, row in signals.iterrows():
            size = self.risk_manager.calculate_position_size(row['signal'], row.get('std', 0.01))
            trade_return = (row['signal'] * row['funding_rate'] * 5  # 5x leverage
                            - 0.0004 - 0.0002)  # Fees + Slippage
            returns.append(trade_return * size)
        return pd.Series(returns)

if __name__ == "__main__":
    credentials = {"BINANCE_API_KEY": "key", "BYBIT_API_KEY": "key", "KRAKEN_API_KEY": "key"}
    analyzer = FundingAnalyzer(["binance", "bybit", "kraken"], ["BTCUSDT", "ETHUSDT"], credentials)
    asyncio.run(analyzer.run())