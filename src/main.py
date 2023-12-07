# Automaded Trading System
# author: Matheus Pedro

import os
from alpha_vantage.timeseries import TimeSeries
import requests
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

def main():
    while True:
        clearPrompt()

        print("------Automated Trading System------")
        print("1 - Real-time analysis of financial market data")
        print("2 - Quit")

        option = input("Choose a feature: ")

        if option == '1':
            clearPrompt()
            realTimeAnalyis()
        elif option == '2':
            clearPrompt()
            quit()
        else:
            clearPrompt()
            print("Just enter your option number!")
            time.sleep(3)

if __name__ == '__main__':
    main()