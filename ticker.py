import requests
import datetime as dt
t = dt.datetime.now()
def get_price(symbol):
    url = 'https://api.binance.com/api/v1/ticker/price'
    params = {
        'symbol': symbol        
    }
    response = requests.get(url, params=params)
    data = response.json()  
    return data['price']

while True:
    delta = dt.datetime.now()-t
    if delta.seconds >= 5:
        print('BTC:'+get_price('BTCUSDT'))
        print('ETH:'+get_price('ETHUSDT'))
        print('------------------')
        t = dt.datetime.now()         
