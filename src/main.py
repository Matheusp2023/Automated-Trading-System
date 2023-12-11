# Automaded Trading System
# author: Matheus Pedro

import os
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import requests
import matplotlib.pyplot as plt
import time

api_key = '7P0IOH3LDW52HMLH'

def clearPrompt():
    operation_system = os.name

    if operation_system == 'posix': # Unix/Linux/MacOS
        os.system('clear')
    elif operation_system == 'nt': # Windows
        os.system('cls')
    else:
        print("Unable to determine operating system to clear prompt")

def realTimeAnalyis():
    symbol = input("Enter the code of the stock you want to analyze: ")
    clearPrompt()
    print("Wait a few seconds before making the next request")

    # TimeSeries class instance with API key
    ts = TimeSeries(key=api_key, output_format='pandas')

    while True:
        try:
            # Get real-time data for action
            data, meta_data = ts.get_quote_endpoint(symbol=symbol)

            # Display price and price change
            price = data['05. price'].iloc[0]
            change = data['09. change'].iloc[0]

            print(f'Symbol: {symbol}, Price: {price}, Change Percentual: {change}')
        except Exception as e:
            print(f"Error getting real-time data: {e}")
        
        # Wait a few seconds before making the next request
        time.sleep(5)

def implementTestTradingStrategies():
    symbol = input("Enter the code of the stock you want to analyze: ")
    print("1 - Crossover Moving Average Strategy")
    print("2 - Day Trading Strategy with Moving Averages")
    print("3 - Buy and Hold Strategy")
    option = input("Choose trading strategy: ")

    if option == '1':
        clearPrompt()
        crossoverMovingAverage(symbol)
    elif option == '2':
        clearPrompt()
        dayTradeStrategy(symbol)
    elif option == '3':
        clearPrompt()
        buyAndHoldStrategy(symbol)
    else:
        clearPrompt()
        print("Just enter your option number!")
        time.sleep(3)
        main()

# Trading strategy
def crossoverMovingAverage(symbol):
    start_date = input("Choose the start date of the analysis [XXXX-XX-XX]: ")
    end_date = input("Choose the end date of the analysis [XXXX-XX-XX]: ")

    print("Please wait...")

    data = yf.download(symbol, start=start_date, end=end_date)

    # Adding Moving Averages
    data['Short_MA'] = data['Close'].rolling(window=50).mean()
    data['Long_MA'] = data['Close'].rolling(window=200).mean()

    # Buy and Sell Signals
    data['Signal'] = 0 #0: No signal, 1: Buy, -1: Sell
    data['Signal'][data['Short_MA'] > data['Long_MA']] = 1
    data['Signal'][data['Short_MA'] < data['Long_MA']] = -1

    # Plotting Results
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', alpha=0.5)
    plt.plot(data['Short_MA'], label='Short Moving Average (50 days)')
    plt.plot(data['Long_MA'], label='Long Moving Average (200 days)')

    # Buy Signal (green) and Sell Signal (red)
    plt.plot(data[data['Signal'] == 1].index, data['Short_MA'][data['Signal'] == 1], '^', markersize=10, color='g', label='Buy')
    plt.plot(data[data['Signal'] == -1].index, data['Short_MA'][data['Signal'] == -1], 'v', markersize=10, color='r', label='Sell')

    plt.title('Crossover Moving Average Strategy')
    plt.legend()
    plt.show()

    result = input("Do you want to buy or sell? [b/s]: ").lower()

    if result == 'b':
        clearPrompt()
        print("Purchase made!")
    elif result == 's':
        clearPrompt()
        print("Sale made!")
    else:
        print("Ação cancelada.")
    
    time.sleep(3)

def dayTradeStrategy(symbol):
    print("Please wait...")

    # Get intraday data
    data = yf.download(symbol, period='1d', interval='1m')

    # Calculate moving averages
    data['Short_MA'] = data['Close'].rolling(window=50).mean()
    data['Long_MA'] = data['Close'].rolling(window=200).mean()

    # Buy and Sell Signals
    data['Signal'] = 0 #0: No signal, 1: Buy, -1: Sell
    data['Signal'][data['Short_MA'] > data['Long_MA']] = 1
    data['Signal'][data['Short_MA'] < data['Long_MA']] = -1

    # Simulate trade execution
    data['Position'] = data['Signal'].diff()

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', alpha=0.5)
    plt.plot(data['Short_MA'], label='Short Moving Average (50 minutes)')
    plt.plot(data['Long_MA'], label='Long Moving Average (200 minutes)')

    # Mark buy (green) and sell (red) points
    plt.scatter(data[data['Position'] == 1].index, data['Short_MA'][data['Position'] == 1], marker='^', color='g', label='Compra')
    plt.scatter(data[data['Position'] == -1].index, data['Short_MA'][data['Position'] == -1], marker='v', color='r', label='Venda')
    
    plt.title('Day Trading Strategy with Moving Averages')
    plt.legend()
    plt.show()

    result = input("Do you want to implement a day trading strategy for this stock? [y/n]: ").lower()

    if result == 'y':
        clearPrompt()
        print("Implemented strategy!")
    elif result == 'n':
        clearPrompt()
        print("Strategy not implemented!")
    else:
        clearPrompt()
        print("Operation canceled!")

    time.sleep(3)

def buyAndHoldStrategy(symbol):
    print("Please wait...")

    # Get historical data
    data = yf.download(symbol, start='2022-01-01', end='2023-01-01')

    # Plot closing price over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', alpha=0.5)
    plt.title('Buy and Hold Strategy')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()

    result = input("Do you want to buy or sell? [b/s]: ").lower()

    if result == 'b':
        clearPrompt()
        print("Purchase made!")
    elif result == 's':
        clearPrompt()
        print("Sale made!")
    else:
        print("Operation canceled!")
    
    time.sleep(3)

def main():
    while True:
        clearPrompt()

        print("------ Automated Trading System ------")
        print("1 - Real-time analysis of financial market data")
        print("2 - Implement and test trading strategies")
        print("3 - Quit")

        option = input("Choose a feature: ")

        if option == '1':
            clearPrompt()
            realTimeAnalyis()
        elif option == '2':
            clearPrompt()
            implementTestTradingStrategies()
        elif option == '3':
            clearPrompt()
            quit()
        else:
            clearPrompt()
            print("Just enter your option number!")
            time.sleep(3)

if __name__ == '__main__':
    main()