class Stock:
    def __init__(self, symbol, current_price=0.0, shares=0):
        self.symbol = symbol
        self.current_price = current_price
        self.shares = shares

    def get_symbol(self):
        return self.symbol

    def get_current_price(self):
        return self.current_price

    def set_current_price(self, price):
        self.current_price = price

    def get_shares(self):
        return self.shares

    def set_shares(self, shares):
        self.shares = shares

    def buy(self, amount):
        self.shares += amount

    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount
        else:
            print("Error: Not enough shares to sell.")

    def get_stock_value(self):
        return self.current_price * self.shares

    def __str__(self):
        return f"Stock: {self.symbol}, Price: {self.current_price}, Shares: {self.shares}"