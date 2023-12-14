# Reporting and Analytics: Detailed reports and analytics on trading performance and market trends
# author: Matheus Pedro da Silva

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def generate_stock_report(ticker, period='1y'):
    # Get stock data using the yfinance library
    stock_data = yf.download(ticker, period=period)

    # Perform basic analysis
    moving_average = stock_data['Close'].rolling(window=20).mean()
    last_quote = stock_data['Close'].iloc[-1]
    last_quote_moving_average = moving_average.iloc[-1]

    # Create visualization (chart)
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], label='Closing Price')
    plt.plot(moving_average.index, moving_average, label='Moving Average (20 days)', linestyle='--')
    plt.title(f'Stock Report - {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

    # Create report
    report = f"""
    Stock Report - {ticker}

    Last Quote: ${last_quote:.2f}
    Moving Average (20 days): ${last_quote_moving_average:.2f}

    Analysis:
    - If the last quote is above the moving average, it may indicate an upward trend.
    - If the last quote is below the moving average, it may indicate a downward trend.
    """

    return report

def reportingAnalyticsFunctionalitie():
    ticker = input("Enter with the symbol of the action: ")
    report = generate_stock_report(ticker)
    print(report)