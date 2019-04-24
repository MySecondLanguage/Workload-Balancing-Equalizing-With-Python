import re

def cleanedDate():
    while True:
        string = input('date :')
        dateValidator = re.compile('(\d{4}\/\d*\/\d*)')
        result = dateValidator.match(string)
        if result is None:
            print('Your Date Pattern is wrong \n it should be dd/mm/yyyy format \n for example 2019/4/30 \n please try again like this')
        else:
            stringList = string.split('/')
            datelist = list(map(int, stringList))
            return datelist
            break

cleanedDate()
