from datetime import datetime

class Transaction:
    def __init__(self, stock_symbol, transaction_type, amount, price):
        self.timestamp = datetime.now()
        self.stock_symbol = stock_symbol
        self.transaction_type = transaction_type  # 'buy' or 'sell'
        self.amount = amount
        self.price = price

    def __str__(self):
        return f"Transaction Type: {self.transaction_type}, Symbol: {self.stock_symbol}, Amount: {self.amount}, Price: {self.price}, Timestamp: {self.timestamp}"