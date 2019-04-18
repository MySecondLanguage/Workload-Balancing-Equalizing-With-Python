import re




def cleanedDate():
    while True:
        string = input('date :')
        dateValidator = re.compile('(\d{2}\/\d{2}\/\d{4})')
        result = dateValidator.match(string)
        if result is None:
            print('Your Date Pattern is wrong \n it should be dd/mm/yyyy format \n please try again')
        else:
            return string
            break

a = cleanedDate()

print(a)