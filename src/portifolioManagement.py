# Portfolio Management: Managing and tracking investment portfolios
# author: Matheus Pedro

import main
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self):
        self.assets = {}

    def add_asset(self, symbol, quantity, price_per_unit):
        if symbol in self.assets:
            self.assets[symbol]['quantity'] += quantity
        else:
            self.assets[symbol] = {'quantity': quantity, 'price_per_unit': price_per_unit}

    def calculate_portfolio_value(self):
        total_value = 0
        for symbol, asset in self.assets.items():
            total_value += asset['quantity'] * asset['price_per_unit']
        return total_value
    
    def plot_pie_chart(self):
        labels = list(self.assets.keys())
        sizes = [asset['quantity'] * asset['price_per_unit'] for asset in self.assets.values()]
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        plt.title('Portfolio Allocation')
        plt.show()

    def print_portfolio(self):
        main.clearPrompt()
        for symbol, asset in self.assets.items():
            print(f"Symbol: {symbol}, Quantity: {asset['quantity']}, Price per Unit: {asset['price_per_unit']}")
            portfolio_value = self.calculate_portfolio_value()
            print(f"Total Portfolio Value: {portfolio_value}")
        while True:
            exit = input("Type b to return to the main menu: ")
            if exit == 'b':
                return

def portfolioManagementFunctionality():
    portfolio = Portfolio()

    portfolio.add_asset('AAPL', 10, 150.0)
    portfolio.add_asset('GOOGL', 5, 2500.0)

    portfolio.plot_pie_chart()
    portfolio.print_portfolio()