#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
i=0
for i in range(1,11):
    my_list.append(random.randint(1,7895))
print(my_list)