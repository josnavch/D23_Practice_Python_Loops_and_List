import random

#Create the function below:
def matrixBuilder(num):
    matrix = []
    for i in range(num):
        col = []
        for j in range(num):
           col.append(1)
        matrix.append(col)
        
    return matrix

print (matrixBuilder(3))