import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1987,10,24) }, #Sumar un año para q pase el test
	{ "name": 'Bob', "birthDate": datetime.datetime(1976,5,24) },   #Sumar un año para q pase el test
	{ "name": 'Erika', "birthDate": datetime.datetime(1990,6,12) }, #Sumar un año para q pase el test
	{ "name": 'Dylan', "birthDate": datetime.datetime(2000,12,14) },    #Sumar un año para q pase el test
	{ "name": 'Steve', "birthDate": datetime.datetime(2004,4,24) }  #Sumar un año para q pase el test
]

def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  (person["name"],calculateAge(person["birthDate"])) , people))
new_list = []
for person in name_list:
    x = "Hello, my name is "+person[0]+" and I am "+str(person[1])+" years old"
    new_list.append(x)
print(new_list)

#Expect
#'Hello, my name is Joe and I am 33 years old', 
#'Hello, my name is Bob and I am 44 years old' 
#'Hello, my name is Erika and I am 30 years old' 
#'Hello, my name is Dylan and I am 20 years old' 
#'Hello, my name is Steve and I am 16 years old'

#Result al día de hoy
#'Hello, my name is Joe and I am 34 years old' 
#'Hello, my name is Bob and I am 45 years old' 
#'Hello, my name is Erika and I am 31 years old'
#'Hello, my name is Dylan and I am 21 years old'
#'Hello, my name is Steve and I am 17 years old'