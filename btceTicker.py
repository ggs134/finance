import requests
import pymongo
import json
import time
from bs4 import BeautifulSoup

def insertData():
    cli = pymongo.MongoClient("52.192.242.11", 27017)
    #cli = pymongo.MongoClient()
    db = cli.ticker

    res = requests.get('https://btc-e.com/api/3/ticker/btc_usd')
    data = json.loads(res.text)
    data['exchangeRate'] = getExRate()
    db.btce.insert(data)
    print data

def getExRate():
    exch = requests.get('http://community.fxkeb.com/fxportal/jsp/RS/DEPLOY_E    XRATE/fxrate_all.html')
    soup = BeautifulSoup(exch.text)
    data  = soup.findAll('td')[20].string
    return float(data)

def main():
    while True:
        insertData()
        time.sleep(60)

if __name__=="__main__":
    main()
