# Automaded Trading System
# author: Matheus Pedro

import os
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

def getDataStock(symbol):
    endpoint = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

    try:
        respose = requests.get(endpoint)
        data = respose.json()

        # Extracting data
        symbol = data['Global Quote']['01. symbol']
        price = data['Global Quote']['05. price']
        change_percent = data['Global Quote']['10. change percent']

        print(f"Symbol: {symbol}, Price: {price}, Change Percentual: {change_percent}%")

    except Exception as e:
        print(f"Error in the socitation: {e}")
        time.sleep(3)
        main()

def realTimeAnalyis():
    symbol = input("Enter the code of the stock you want to analyze: ")
    clearPrompt()
    print("The information will be updated every 1 minute")

    # Continuous updates
    while True:
        informations = getDataStock(symbol)
        print(informations)

        # Wait 1 minute before making the next request
        time.sleep(60)

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