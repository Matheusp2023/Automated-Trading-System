from abc import ABC, abstractmethod
import numpy as np

# Implementação da Interface de Implementação
class TradingStrategyImplementation(ABC):
    @abstractmethod
    def execute_strategy(self):
        pass

# Implementação Concreta para Média Móvel Simples (SMA)
class SimpleMovingAverageStrategy(TradingStrategyImplementation):
    def __init__(self, stock, trader, quantity, short_window=10, long_window=50):
        self.stock = stock
        self.trader = trader
        self.quantity = quantity
        self.short_window = short_window
        self.long_window = long_window

    def execute_strategy(self):
        data = self.stock.getStockData()
        prices = data['Close'].tolist()
        short_sma = self.calculate_sma(prices, self.short_window)
        long_sma = self.calculate_sma(prices, self.long_window)

        if short_sma > long_sma:
            self.trader.buyStock(self.stock, self.quantity)
        elif short_sma < long_sma:
            self.trader.sellStock(self.stock, self.quantity)
        else:
            print("Nenhum sinal de negociação")

    def calculate_sma(self, prices, window):
        if len(prices) < window:
            return np.nan
        else:
            return np.mean(prices[-window:])

# Implementação Concreta para Índice de Força Relativa (RSI)
class RelativeStrengthIndexStrategy(TradingStrategyImplementation):
    def __init__(self, stock, trader, quantity, rsi_period=14, overbought_threshold=70, oversold_threshold=30):
        self.stock = stock
        self.trader = trader
        self.quantity = quantity
        self.rsi_period = rsi_period
        self.overbought_threshold = overbought_threshold
        self.oversold_threshold = oversold_threshold

    def execute_strategy(self):
        data = self.stock.getStockData()
        prices = data['Close'].tolist()
        rsi = self.calculate_rsi(prices, self.rsi_period)
        last_rsi = rsi[-1]

        if last_rsi > self.overbought_threshold:
            self.trader.sellStock(self.stock, self.quantity)
        elif last_rsi < self.oversold_threshold:
            self.trader.buyStock(self.stock, self.quantity)
        else:
            print("Nenhum sinal de negociação")

    def calculate_rsi(self, prices, period):
        delta = np.diff(prices)
        gain = delta * 0
        loss = gain.copy()

        gain[delta > 0] = delta[delta > 0]
        loss[delta < 0] = -delta[delta < 0]

        avg_gain = self.smoothed_average(gain, period)
        avg_loss = self.smoothed_average(loss, period)

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def smoothed_average(self, data, window):
        weights = np.ones(window) / window
        return np.convolve(data, weights, mode='valid')

# Abstração
class TradingStrategy:
    def __init__(self, implementation):
        self._implementation = implementation

    def execute(self):
        self._implementation.execute_strategy()
