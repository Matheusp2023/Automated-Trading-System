# Buy/Sell Order Execution
# # author: Matheus Pedro

import yfinance as yf
import time
import main

class Stock:
    def __init__(self, symbol, current_price, price_maximum, price_minimum, target_return):
        self.symbol = symbol
        self.current_price = current_price
        self.price_maximum = price_maximum
        self.price_minimum = price_minimum
        self.target_return = target_return

# Define functions to buy and sell stocks
def buyStock(symbol, quantity):
    print(f"Buying {quantity} shares of {symbol} at market price.")

def sellStock(symbol, quantity):
    print(f"Selling {quantity} shares of {symbol} at market price.")

# Calculates the price_target for selling a share
def calcPriceTarget(price, target_return):
    # Calculate target price
    price_target = price * (1 + target_return)

    return price_target


# Define criteria for buy and sell orders
def buyCriteria(current_price, price_maximum, price_minimum):
    # Define your buy criteria
    if (current_price > price_minimum) & (current_price < price_maximum):
        return True
    else:
        return False

def sellCriteria(current_price, target_return):
    # Define your sell criteria
    if current_price < calcPriceTarget(current_price, target_return):
        return True
    else:
        return False

def buySellOrderExecutionFunctionality():
    # Define symbols to monitor
    symbols = []
    stocks = []

    print("What actions do you want to monitor (type r to stop)")
    definitionSymbols = True

    while definitionSymbols:
        symbol = input("Type the stock symbol and enter: ")
        if symbol == 'r':
            definitionSymbols = False
        else:
            symbols.append(symbol)

    buy_quantity = int(input("Enter the quantity you wish to purchase: "))
    sell_quantity = int(input("Enter the quantity you want to sell: "))

    for symbol in symbols:
        main.clearPrompt()

        # Get current stock price
        stock_data = yf.download(symbol, period="1d", interval="1m")
        current_price = stock_data["Close"][-1]
        price_maximum = float(input(f"Enter the maximum price to {symbol}: "))
        price_minimum = float(input(f"Enter the minimum price to {symbol}: "))
        target_return = float(input(f"Enter the desired return (in US$) to {symbol}: "))

        stock = Stock(symbol, current_price, price_maximum, price_minimum, target_return)
        stocks.append(stock)

    main.clearPrompt()
    
    # Continuously monitor symbols for buy/sell opportunities
    while True:
        for stock in stocks:
            # Check buy criteria
            if buyCriteria(stock.current_price, stock.price_maximum, stock.price_minimum):
                buyStock(stock.symbol, buy_quantity)

            # Check sell criteria
            elif sellCriteria(stock.current_price, stock. target_return):
                sellStock(stock.symbol, sell_quantity)

        # Wait for some time before checking again
        time.sleep(3)