import csv
from datetime import datetime

def readCSV(filename):
    with open(filename, "r") as csvf:
        csv_reader = csv.reader(csvf)
        for row in csv_reader:
            yield row



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


def zGroup(xFile):
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

def main(xFile, yFile, zFile):
    xGroup(xFile)
    yGroup(yFile)
    zGroup(zFile)


if __name__ == '__main__':
    xFile = 'x.csv'
    yFile = 'y.csv'
    zFile = 'z.csv'
    main(xFile, yFile, zFile)