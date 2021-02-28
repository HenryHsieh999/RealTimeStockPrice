from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt

currentStocks = ['ESE.V', 'SHOP.TO', 'CGX.TO', 'AC.TO']

def real_time_price(ticker):
    url = ('https://ca.finance.yahoo.com/quote/') + ticker + ('?p=') + ticker
    r=requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})
    price = web_content.find('span').text

    if web_content == []:
        web_content = '99999'
    return price

# for step in range(1, 101):
while True:
    price = []
    col = []
    time_stamp = dt.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for ticker in currentStocks:
        price.append(ticker + " " + real_time_price(ticker))
    col = [time_stamp]
    col.extend(price)
    # df = pd.DataFrame(col)
    # df = df.T
    # df.to_csv('Real time stock data.csv', mode='a', header = False)
    print(col)
