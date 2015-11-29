import pymongo
import numpy as np

#database
db = pymongo.MongoClient()['finance']
#company list
company_list = db.finance.distinct('company')


arr = None
arr1 = None
#make array
for j in company_list:
    if j == 2:
        continue
    row = []
    print j
    for i in db.finance.find({'company':j},{'Open':1}):
        row.append(i['Open'])
    
    if arr is None:
        arr = np.array(row)
    elif arr1 is None:
        row=[]
        continue

    arr1 = np.array(row)
    np.vstack((arr,arr1))
    row = []
