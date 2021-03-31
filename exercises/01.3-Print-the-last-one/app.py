# import the random package here "import random"
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()

# Feel happy to write the code below this comment, good luck!:
the_last_one = len(my_stupid_list)
print (my_stupid_list[the_last_one - 1])