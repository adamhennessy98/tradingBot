import requests
import json
from config import *


URL_BASE = "https://paper-api.alpaca.markets"
URL_ACCOUNT = "{}/v2/account".format(URL_BASE)
ORDERS_URL = "{}/v2/orders".format(URL_BASE)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET_KEY}


def get_account():
    r = requests.get(URL_ACCOUNT, headers=HEADERS)

    return json.loads(r.content)


def create_order(symbol, qty, side, typee, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": typee,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)


response = create_order("AAPL", 100, "buy", "market", "gtc")
print(response)