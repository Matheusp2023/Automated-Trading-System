# Real-Time Alerts and Notifications: Notifications about market events and portfolio changes
# author: Matheus Pedro

import websocket
import json
import requests
from alpha_vantage.timeseries import TimeSeries

PUSHBULLET_API_KEY = 'o.udHAnymJivQWVdOjFxz7nUrRkGl8Zt0G'
PUSHBULLET_URL = 'https://api.pushbullet.com/v2/pushes'

ALPHA_VANTAGE_API_KEY = '7P0IOH3LDW52HMLH'

def send_pushbullet_notification(title, body):
    headers = {'Access-Token': PUSHBULLET_API_KEY, 'Content-Type': 'application/json'}
    data = {'type': 'note', 'title': title, 'body': body}
    response = requests.post(PUSHBULLET_URL, headers=headers, data=json.dumps(data))
    return response.json()

def on_message(ws, message, symbol):
    print(f'Message received: {message}')
    data = json.loads(message)
    
    # Extracting relevant information from the message
    price = data['lastTrade']['price']
    
    title = f'Action Alert - {symbol}'
    body = f'New price for {symbol}: {price}'
    
    # Send notification via Pushbullet
    send_pushbullet_notification(title, body)

def on_error(ws, error):
    print(f'Erro: {error}')

def on_close(ws, close_status_code, close_msg):
    print(f'Connection closed: {close_status_code}, {close_msg}')

def on_open(ws):
    print('Open connection')

def realTimeAlertsNotificationsFunctionalitie():
    symbol = input("Enter the symbol of the stock you want to receive notification of: ")
    WEBSOCKET_URL = f'wss://streamer.finance.yahoo.com/quote/{symbol}?format=json'

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WEBSOCKET_URL, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()