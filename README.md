# XMR Mining Monitor

A Python dashboard for monitoring Monero (XMR) mining stats via the Nanopool API.  
Fetches live worker data and visualizes hashrate trends with matplotlib.

## Features

- Live balance and hashrate from Nanopool API
- Chart — all workers × all time windows
- Chart — current hashrate per worker
- Chart — account-level average hashrate over time
- Saves dashboard as PNG

## Setup

```bash
git clone https://github.com/Fakiri-ismail/xmr-mining-monitor.git
cd xmr-mining-monitor

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Configuration

Set your wallet address in `.env` :

```ini
WALLET_ADDRESS=your_xmr_wallet_address_here
```

## Run

```bash
python -m src.main
```

The dashboard is saved as `nanopool_dashboard.png` and displayed on screen.

## Dev

```bash
pip install -r requirements.txt
pytest                  # run tests
black src/ tests/       # format
flake8 src/ tests/      # lint
```

## Project structure

```
xmr-mining-monitor/
├── src/
│   ├── __init__.py
│   ├── fetcher.py       # Nanopool API calls
│   ├── visualizer.py    # matplotlib charts
│   └── main.py          # entry point
├── tests/
│   └── test_fetcher.py
├── .env                 # wallet address (never commit)
├── .gitignore
├── requirements.txt
└── README.md
```