"""Fetch the current price of a single ticker from Yahoo Finance."""

import yfinance as yf

TICKER = "AAPL"

stock = yf.Ticker(TICKER)
price = stock.info["currentPrice"]

print(f"{TICKER}: S{price:.2f}")
