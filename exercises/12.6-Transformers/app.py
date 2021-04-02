incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
transformedData = ""
def my_var(items):
    transformedData = items["name"] + " " + items["lastName"]
    return transformedData

name_list = list(map(my_var, incomingAJAXData))
print (name_list)
