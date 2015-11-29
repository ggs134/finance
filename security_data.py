import pandas as pd
import pymongo
import pandas.io.data as web
import datetime

#DB Client
cli = pymongo.MongoClient()
db = cli.finance

#Read google code and company's name
sec = pd.read_csv('KRX_security.csv')
sec1 = sec[['company_name','google_code']]
sec10 = sec1[1:10]


start = datetime.datetime(2014,1,1)
end = datetime.datetime(2014,12,31)

for record in sec10.to_records(): 
    collection = db['finance']
    f = web.DataReader(record[2], 'google', start, end)
    for i in range(len(f.index)):
        row = f.ix[i]
        collection.insert({'company':record[1].decode('utf-8'),'time':f.index[i], 'Open':row[0], 'High':row[1], 'Low':row[2], 'Close':row[3], 'Volume':row[4]})


    
