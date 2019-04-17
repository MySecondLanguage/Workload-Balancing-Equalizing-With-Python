import csv
from datetime import datetime
import pendulum

def readCSV(filename):
    with open(filename, "r") as csvf:
        csv_reader = csv.reader(csvf)
        for row in csv_reader:
            yield row


def getLastGroup(filename):
    row = readCSV(filename)
    groupList = []
    for group in row:
        group = group[-1]
        groupList.append(group)
    return groupList[-1]

def getPreviousGroup(filename):
    row = readCSV(filename)
    groupList = []
    for group in row:
        group = group[-1]
        groupList.append(group)
    return groupList[-1]



def getLastDay(filename):
    row = readCSV(filename)
    dateList = []
    for date in row:
        date = date[0]
        dateList.append(date)
    return dateList[-1]

def getPreviousDay(filename):
    row = readCSV(filename)
    dateList = []
    for date in row:
        date = date[0]
        dateList.append(date)
    return dateList[-2]






def xGroup(xFile):
    today = datetime.today().strftime('%d/%m/%Y')
    employe_dict = {}
    employe_dict['date'] = today

    row = readCSV(xFile)
    ID_LIST = []
    NAME_LIST = []
    for id, name in row:
        ID_LIST.append(id)
        NAME_LIST.append(name)

    employe_dict['e1_id'] = ID_LIST[0]
    employe_dict['e1_name'] = NAME_LIST[0]

    employe_dict['e2_id'] = ID_LIST[1]
    employe_dict['e2_name'] = NAME_LIST[1]

    employe_dict['e3_id'] = ID_LIST[2]
    employe_dict['e3_name'] = NAME_LIST[2]
    employe_dict['group'] = 'groupX'

    #print(employe_dict)

    field_name = ['date', 'e1_id', 'e1_name', 'e2_id', 'e2_name', 'e3_id', 'e3_name', 'group']
    with open("output.csv", "a", encoding="UTF-8") as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=field_name)
        # csv_writer.writeheader(field_name)
        csv_writer.writerow(employe_dict)


def yGroup(yFile):
    today = datetime.today().strftime('%d/%m/%Y')
    employe_dict = {}
    employe_dict['date'] = today

    row = readCSV(yFile)
    ID_LIST = []
    NAME_LIST = []
    for id, name in row:
        ID_LIST.append(id)
        NAME_LIST.append(name)

    employe_dict['e1_id'] = ID_LIST[0]
    employe_dict['e1_name'] = NAME_LIST[0]

    employe_dict['e2_id'] = ID_LIST[1]
    employe_dict['e2_name'] = NAME_LIST[1]

    employe_dict['e3_id'] = ID_LIST[2]
    employe_dict['e3_name'] = NAME_LIST[2]
    employe_dict['group'] = 'groupY'

    #print(employe_dict)

    field_name = ['date', 'e1_id', 'e1_name', 'e2_id', 'e2_name', 'e3_id', 'e3_name', 'group']
    with open("output.csv", "a", encoding="UTF-8") as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=field_name)
        # csv_writer.writeheader(field_name)
        csv_writer.writerow(employe_dict)


def zGroup(zFile):
    today = datetime.today().strftime('%d/%m/%Y')
    employe_dict = {}
    employe_dict['date'] = today

    row = readCSV(xFile)
    ID_LIST = []
    NAME_LIST = []
    for id, name in row:
        ID_LIST.append(id)
        NAME_LIST.append(name)

    employe_dict['e1_id'] = ID_LIST[0]
    employe_dict['e1_name'] = NAME_LIST[0]

    employe_dict['e2_id'] = ID_LIST[1]
    employe_dict['e2_name'] = NAME_LIST[1]

    employe_dict['e3_id'] = ID_LIST[2]
    employe_dict['e3_name'] = NAME_LIST[2]
    employe_dict['group'] = 'groupZ'

    #print(employe_dict)

    field_name = ['date', 'e1_id', 'e1_name', 'e2_id', 'e2_name', 'e3_id', 'e3_name', 'group']
    with open("output.csv", "a", encoding="UTF-8") as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=field_name)
        # csv_writer.writeheader(field_name)
        csv_writer.writerow(employe_dict)

def main(filename):

    xFile = 'x.csv'
    yFile = 'y.csv'
    zFile = 'z.csv'

    today = pendulum.today().strftime('%d/%m/%Y')
    lastDay = getLastDay(filename)
    previousDay = getPreviousDay(filename)
    lastGroup = getLastGroup(filename)
    previousGroup = getPreviousDay(filename)


    if lastDay < today and lastGroup == 'groupZ':
        print('next job for GroupX')
        xGroup(xFile)
    elif lastDay < today and lastGroup == 'groupX':
        print('next jobs for groupY')
        yGroup(yFile)
    elif lastDay < today and lastGroup == 'groupY':
        print('next job for groupZ')
        zGroup(zFile)
    else:
        print("today's job already been done")


output = 'output.csv'
main(output)

