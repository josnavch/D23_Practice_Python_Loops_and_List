arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
#Your code go here:

def sumOdds (array):
    total_odd = 0
    for i in array:
        if i % 2 != 0:
            total_odd += i
    print (total_odd)

sumOdds(arr)

