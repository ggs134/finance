import requests
import pymongo
import json
import time
import telepot
#from bs4 import BeautifulSoup

def insertData():
    cli = pymongo.MongoClient("192.168.1.19", 27017)
    #cli = pymongo.MongoClient()
    db = cli.ticker
    
    #Get Btc-e Data
    btceResult = requests.get('https://btc-e.com/api/3/ticker/btc_usd')
    #Get Korbit Data
    korbitResult = requests.get('https://api.korbit.co.kr/v1/ticker/detailed')

    #parse data
    btceData = json.loads(korbitResult.text)
    korbitData = json.loads(btceResult.text)
    
    result = {}
    
    result['korbit']=korbitData
    result['btce']=btceData
    result['time']=time.time()    
    db.btce.insert(result)
    print result

def getExRate():
    exch = requests.get('http://community.fxkeb.com/fxportal/jsp/RS/DEPLOY_E    XRATE/fxrate_all.html')
    soup = BeautifulSoup(exch.text)
    data  = soup.findAll('td')[20].string
    return float(data)

def main():
    try:
        while True:
            insertData()
            time.sleep(5)
    except Exception as e:
        bot = telepot.Bot('155578772:AAGngKO2rPtjzC2_P3CM7FSsL-FIAfzRk8A')
        bot.sendMessage(33612976, "Error Occured\n"+str(e))
        print e

if __name__=="__main__":
    main()
