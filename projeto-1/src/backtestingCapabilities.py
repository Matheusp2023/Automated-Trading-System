# Backtesting Capabilities: Testing trading strategies against historical market data
# author: Matheus Pedro

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to perform backtesting
def backtest(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)

    data['Signal'] = 0
    data['Signal'][data['Close'] > data['Close'].shift(1)] = 1
    data['Signal'][data['Close'] < data['Close'].shift(1)] = -1

    # Calculate the accumulated return of the strategy
    data['Strategy Returns'] = data['Signal'].shift(1) * data['Close'].pct_change()
    data['Cumulative Strategy Returns'] = (1 + data['Strategy Returns']).cumprod()

    # Calculate the accumulated return on the asset
    data['Asset Returns'] = data['Close'].pct_change()
    data['Cumulative Asset Returns'] = (1 + data['Asset Returns']).cumprod()

    # Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(data['Cumulative Strategy Returns'], label='Estratégia de Day Trade')
    plt.plot(data['Cumulative Asset Returns'], label='Ativo')
    plt.legend()
    plt.show()

def backtestingCapabilitiesFunctionalities():
    print("Backtest the day trade strategy")
    symbol = input("Enter the action symbol: ")

    backtest(symbol, start_date='2022-01-01', end_date='2023-01-01')