import datetime as dt
import pandas as pd

x = ['jhon doe', 'GX']

y = ['donald ted', 'GY']

Z = ['smith joe', 'GZ']

start_date = dt.datetime(2019, 4,12)
end_date = dt.datetime(2019, 4,21)
daterange = pd.date_range(start_date, end_date)

i=0
for date in daterange:
    if i % 3 == 0:
        print (date.strftime('%d/%m/%Y'), *x, sep=',')
    elif i % 3 == 1:
        print (date.strftime('%d/%m/%Y'), *y, sep=',')
    else:
        print (date.strftime('%d/%m/%Y'), *Z, sep=',')
    i+=1