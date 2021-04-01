
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
hello = []

#your code go here:
for i in my_list:
    if type(i) is dict:
        hello.append(i)
    elif type(i) is list:
        hello.append(i)

print(hello)

