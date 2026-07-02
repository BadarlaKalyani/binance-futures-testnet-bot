# Binance Futures Testnet Trading Bot

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- API Key & Secret

## Installation

```bash
pip install -r requirements.txt
```

## Configure

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Features

- Market Orders
- Limit Orders
- BUY / SELL
- CLI Interface
- Logging
- Exception Handling