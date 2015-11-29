import pandas.io.data as web
import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2010,12,31)

f = web.DataReader("F", 'yahoo',start, end)
print f
