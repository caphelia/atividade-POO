#Projeto Final

#pip install backtrader
#pip install --upgrade yfinance

import backtrader as bt
import yfinance as yf
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


class Estratégia(bt.Strategy):
    params = (
        ("period", 50),
        ("threshold", 0.03),
    )
    def __init__(self):
        self.average = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period)
    
    def next(self):
        current_price = self.data.close[0]
        price_deviation = (current_price - self.average[0]) / self.average[0]

        if price_deviation > self.params.threshold:
            if not self.position:
                self.sell()
        elif price_deviation < -self.params.threshold:
            if not self.position:
                self.buy()

ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-01-01'

data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0) 

data_feed = bt.feeds.PandasData(dataname=data)

cerebro = bt.Cerebro()
cerebro.adddata(data_feed)
cerebro.addstrategy(Estratégia)

initial_cash = 15000

cerebro.broker.set_cash(initial_cash)

cerebro.run()

final_cash = cerebro.broker.getvalue()

print(f'Saldo inicial: ${initial_cash:.2f}')
print(f'Saldo final: ${final_cash:.2f}')
print(f'Lucro/Prejuízo: ${final_cash - initial_cash:.2f}')
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data_feed = bt.feeds.PandasData(dataname=data)

cerebro = bt.Cerebro()
cerebro.adddata(data_feed)
cerebro.addstrategy(Estratégia)

initial_cash = 15000

cerebro.broker.set_cash(initial_cash)

cerebro.run()

final_cash = cerebro.broker.getvalue()

print(f'Saldo inicial: ${initial_cash:.2f}')
print(f'Saldo final: ${final_cash:.2f}')
print(f'Lucro/Prejuízo: ${final_cash - initial_cash:.2f}')
