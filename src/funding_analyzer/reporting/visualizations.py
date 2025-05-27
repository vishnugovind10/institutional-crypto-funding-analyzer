import matplotlib.pyplot as plt
import logging

logging.basicConfig(filename='logs/funding_analyzer.log', level=logging.INFO)

def plot_results(data, returns, metrics):
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
        ax1.plot(data['timestamp'], data['funding_rate'], marker='o', label='Funding Rate')
        ax1.set_title('Funding Rates Over Time')
        ax1.set_ylabel('Funding Rate')
        ax1.legend()
        ax2.plot(data['timestamp'], returns.cumsum(), marker='o', color='green', label='Cumulative Return')
        ax2.set_title(f'Backtest Performance (Sharpe: {metrics["sharpe_ratio"]:.2f})')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Cumulative Return')
        ax2.legend()
        plt.tight_layout()
        plt.savefig('data/backtest_plot.png')
        plt.show()
        logging.info("Plots generated")
    except Exception as e:
        logging.error(f"Plotting failed: {e}")