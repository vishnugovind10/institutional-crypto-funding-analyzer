# Institutional Crypto Funding Rate Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A professional-grade tool for crypto hedge funds to analyze funding rates, backtest strategies, and manage risks across multiple exchanges.

## Features
- **Supported Exchanges**: Binance, Bybit, Kraken (real-time and historical data)
- **Real-Time Data**: WebSocket feeds with sub-second latency
- **Backtesting**: Includes leverage, fees, slippage, and stress testing
- **Risk Management**: VaR, CVaR, position sizing, and stress scenarios
- **Strategies**: Statistical arbitrage, cross-exchange arbitrage, momentum
- **Portfolio Tools**: Multi-strategy aggregation and risk reporting
- **Alerts**: Slack, Email, WhatsApp, Signal notifications

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/institutional-crypto-funding-analyzer.git
   cd institutional-crypto-funding-analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API keys in `config/.env` (see `.env.template`).
4. Run the setup script:
   ```bash
   python scripts/setup.py
   ```

## Usage
```bash
python -m src.funding_analyzer.core.analyzer
```
- Fetches real-time funding rates
- Runs a default statistical arbitrage backtest
- Generates plots and CSV reports

## Configuration
Edit `config/config.yaml` for:
- Exchange API keys
- Trading parameters (leverage, fees, slippage)
- Notification settings

## Sample Data
Test with `data/sample_funding_rates.csv` if API keys are unavailable.

## License
MIT License

## Disclaimer
For educational and research purposes only. Trading involves significant risk.