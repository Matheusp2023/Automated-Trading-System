import Stock

class Trader:
    def __init__(self, name):
        self.name = name
        self.portfolio = {}

    def buy_stock(self, stock_symbol, amount, price):
        if stock_symbol in self.portfolio:
            self.portfolio[stock_symbol].buy(amount)
        else:
            new_stock = Stock(symbol=stock_symbol, current_price=price, shares=amount)
            self.portfolio[stock_symbol] = new_stock

    def sell_stock(self, stock_symbol, amount):
        if stock_symbol in self.portfolio:
            self.portfolio[stock_symbol].sell(amount)
            if self.portfolio[stock_symbol].get_shares() == 0:
                del self.portfolio[stock_symbol]
        else:
            print("Error: Stock not found in the portfolio.")

    def get_portfolio_value(self):
        total_value = 0.0
        for stock in self.portfolio.values():
            total_value += stock.get_stock_value()
        return total_value

    def __str__(self):
        return f"Trader: {self.name}, Portfolio Value: ${self.get_portfolio_value()}"