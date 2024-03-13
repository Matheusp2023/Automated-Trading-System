class Transaction:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type, symbol, quantity, price):
        transaction = {
            "type": transaction_type,
            "symbol": symbol,
            "quantity": quantity,
            "price": price
        }
        self.transactions.append(transaction)

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"Type: {transaction['type']}, Symbol: {transaction['symbol']}, Quantity: {transaction['quantity']}, Price: {transaction['price']}")