import requests
import time
import json
import random

testtext = requests.get("https://blockchain.info/ru/ticker").text

d = json.loads(testtext)
s = input()
dopd = {}
while True:
    d[s].update({'15m': random.randint(10,100),
                     'last': random.randint(10,100),
                     'buy':random.randint(10,100),
                     'sell':random.randint(10,100)
                })
    dopd = d[s]
    print(dopd['buy'])
    time.sleep(5)
