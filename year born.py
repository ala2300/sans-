import datetime
now = datetime.datetime.now()
age = float(input('how old are you? '))
year =  int(now.year - age)
print ("you were born in ", year)
