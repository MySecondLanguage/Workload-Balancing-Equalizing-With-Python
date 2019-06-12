import datetime as dt
import pandas as pd
import csv

start_date = dt.datetime(2019, 4,12)
end_date = dt.datetime(2019, 4,21)
daterange = pd.date_range(start_date, end_date)


XLIST = ['401', 'Pabolo Picasso', '402', 'Justin TED', '303', 'Ariana Great']
YLIST = ['201', 'Donald Ted', '202', 'Einastain', '203', 'Hillary Cloud']
ZLIST = ['301', 'Theresa March', '302', 'Jullian Ass Bad', '303', 'Messi Bro']


i = 0
for date in daterange:
    if i % 3 == 0:
        x = [str(date)] + XLIST
        print(x)
        with open("test.csv", 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(x)
    elif i % 3 == 1:
        y = [str(date)] + YLIST
        print(y)
        with open("test.csv", 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(y)
    else:
        z = [str(date)] + ZLIST
        print(z)
        with open("test.csv", 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(z)
    i+=1
