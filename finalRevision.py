import datetime as dt
import pandas as pd
import csv
import re

def readCSV(filename):
    with open(filename, "r") as csvf:
        csv_reader = csv.reader(csvf)
        for row in csv_reader:
            yield row

def startProcessedDate():
    while True:
        string = input('Start date yyyy/mm/dd :')
        dateValidator = re.compile('(\d{4}\/\d*\/\d*)')
        result = dateValidator.match(string)
        if result is None:
            print('Your Date Pattern is wrong \n it should be dd/mm/yyyy format \n for example 2019/4/30 \n and never put zero before day or manth \n please try again like this')
        else:
            stringList = string.split('/')
            datelist = list(map(int, stringList))
            return datelist
            break


def endProcessedDate():
    while True:
        string = input('End date yyyy/mm/dd :')
        dateValidator = re.compile('(\d{4}\/\d*\/\d*)')
        result = dateValidator.match(string)
        if result is None:
            print('Your Date Pattern is wrong \n it should be dd/mm/yyyy format \n for example 2019/4/30 \n and never put zero before day or manth \n please try again like this')
        else:
            stringList = string.split('/')
            datelist = list(map(int, stringList))
            return datelist
            break



def makeOneList(filename):
    oneList = []
    eList = readCSV(filename)
    for id, name in eList:
        oneList.append(id)
        oneList.append(name)
    return oneList


def main(xfile, yfile, zfile):
    XLIST = makeOneList(xfile)
    YLIST = makeOneList(yfile)
    ZLIST = makeOneList(zfile)

    start_date_list = startProcessedDate()
    end_date_list = endProcessedDate()

    start_year = start_date_list[0]
    start_month = start_date_list[1]
    start_day = start_date_list[2]

    end_year = end_date_list[0]
    end_month = end_date_list[1]
    end_day = end_date_list[2]

    start_date = dt.datetime(start_year, start_month, start_day)
    end_date = dt.datetime(end_year, end_month, end_day)
    daterange = pd.date_range(start_date, end_date)

    i = 0
    for date in daterange:
        if i % 3 == 0:
            x = [str(date)] + XLIST
            print(x)
            with open("output.csv", 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(x)
        elif i % 3 == 1:
            y = [str(date)] + YLIST
            print(y)
            with open("output.csv", 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(y)
        else:
            z = [str(date)] + ZLIST
            print(z)
            with open("output.csv", 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(z)
        i += 1

if __name__ == '__main__':
    x = 'x.csv'
    y = 'y.csv'
    z = 'z.csv'
    main(x, y, z)



