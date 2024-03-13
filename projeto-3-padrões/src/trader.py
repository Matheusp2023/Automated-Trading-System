import transaction
import matplotlib.pyplot as plt

class Trader:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.portfolio = {}
        self.transaction_log = transaction.Transaction()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient balance.")
            return False

    def buyStock(self,  stock, quantity):
        cost = stock.price * quantity
        if cost <= self.balance:
            stock.buy(quantity)
            if stock.symbol in self.portfolio:
                self.portfolio[stock.symbol][0] += quantity
            else:
                self.portfolio[stock.symbol] = [quantity, stock.price]
            self.balance -= cost
            self.transaction_log.add_transaction("BUY", stock.symbol, quantity, stock.price)
            print(f"Bought {quantity} shares of {stock.symbol} at ${stock.price} each.")
            stock.quantity += quantity
            return True
        else:
            print("Insufficient funds to buy.")
            return False

    def sellStock(self, stock, quantity):
        if stock.symbol in self.portfolio and self.portfolio[stock.symbol][0] >= quantity:
            stock.sell(quantity)
            self.balance += quantity * stock.price
            self.portfolio[stock.symbol][0] -= quantity
            self.transaction_log.add_transaction("SELL", stock.symbol, quantity, stock.price)
            print(f"Sold {quantity} shares of {stock.symbol} at ${stock.price} each.")
            stock.quantity -= quantity
            if self.portfolio[stock.symbol][0] == 0:
                del self.portfolio[stock.symbol]
            return True
        else:
            print("Insufficient shares to sell or stock not found in portfolio.")
            return False

    def displayPortfolio(self):
        print(f"Portfolio for {self.name}:")
        for symbol, (quantity, price) in self.portfolio.items():
            print(f"{symbol}: {quantity} shares at ${price} each")
        print(f"Balance: ${self.balance}")

    def plotPortfolioPieChart(self):
        labels = list(self.portfolio.keys())
        sizes = [self.portfolio[symbol][0] for symbol in labels]

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f'Portfolio Distribution for {self.name}')
        plt.show()