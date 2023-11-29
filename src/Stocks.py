# Stocks class


class Stocks():
    def __init__(self, name, code, price, quotas, valuation, profit, assets):
        self.name = name
        self.code = code
        self.price = float(price)
        self.quotas = int(quotas)
        self.valuation = float(valuation)
        self.profit = float(profit)
        self.assets = float(assets)
        self.earningsYear = 0

    def getPL(self, price, profit, quotas):
        return price / (profit / quotas)
    
    def getPVP(self, price, valuation):
        return price / valuation
    
    def getDY(self, earningsYear, price):
        return earningsYear / price
    
    def getROE(self, profit, assets):
        return profit / assets