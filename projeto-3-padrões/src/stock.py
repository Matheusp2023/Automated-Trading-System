import yfinance as yf
import schedule
import time
import threading

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 0.00
        self.quantity = 0

        self.updatePriceStock()
        self.startUpdateThread()

    def buy(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        self.quantity -= quantity

    def getStockData(self):
        data = yf.download(self.symbol, start="2024-01-01", end="2024-03-13")
        return data
    
    def updatePriceStock(self):
        data = self.getStockData()
        latest_data = data.iloc[-1]
        self.price = latest_data['Adj Close']
    
    def display(self):
        print("Stock Symbol:", self.symbol)
        print("Stock Price:", self.price)
        print("Quantity Available:", self.quantity)

    def updatePricePeriodically(self):
        self.updatePriceStock()

    def taskUpdatePrice(self):
        schedule.every(1).minutes.do(self.updatePricePeriodically)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def startUpdateThread(self):
        update_thread = threading.Thread(target=self.taskUpdatePrice)
        update_thread.daemon = True  # O thread será finalizado quando o programa principal terminar
        update_thread.start()