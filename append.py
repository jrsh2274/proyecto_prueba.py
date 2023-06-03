# append agrega un elemento + en una lista
# ramdom numero aleatorio
import numpy as np
import random as rd
a = []
for i in range (10):
    a.append(rd.randint(0,100))
b= np.array(a)
print(b)