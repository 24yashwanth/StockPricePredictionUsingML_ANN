
# Raw Package
import numpy as np
import pandas as pd
import time

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def show_chart(data):
    #declare figure
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title='Uber live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    #Show
    fig.show()

def extractData(stockName=None,period=None,interval=None,start=None,end=None):
    if(period!=None):
        data = yf.download(tickers=stockName, period=period, interval=interval)
    else:
        data = yf.download(tickers=stockName, start="2009-05-04", end="2020-05-04", interval=interval)
    return data
    
stockName = 'UBER'
data=extractData(stockName='TSLA',period='1d',interval='1m')

for i in data:print(i)
while(True):
    data=extractData(stockName='TSLA',period='10y',interval='1m')
    # data=extractData(stockName='TATASTEEL',start="2009-05-04", end="2020-05-04",interval='1m')
    open = data['Open'],
    high = data['High']
    low = data['Low'],
    close = data['Close']
    adjClose = data['Adj Close']
    volume = data['Volume']


    highLow = []
    openClose = []
    for H,L in zip(high,low):
        highLow.append(H-L)
    for O,C in zip(open,close):
        openClose.append(O-C)
    # print(highLow,end = "\n\n\n")
    # print(openClose,end = "\n\n\n")
    sevenDaysMA = data.rolling(window=7).mean()
    fourteenDaysMA = data.rolling(window=14).mean()
    twentyoneDaysMA = data.rolling(window=21).mean()
    sevenDaysSD = data.rolling(window=7).std()
    # print(sevenDaysMA)
    # for i in sevenDaysMA:
    #     print(sevenDaysMA[i])
    print(data)
    
    
    
    time.sleep(55)