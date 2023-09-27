import math
import random
import matplotlib.pyplot as plt
import numpy as np


dataSet = []
c = []
dataSetLenght = 1000

def customFct(x):
    y = (x[0]*2.4 + x[1]*5.5)**2
    return round(y)

def fillData(d):
    for i in range(dataSetLenght):
        d.append([random.random()*10,random.random()*10])
        c.append(customFct(d[-1]))


fillData(dataSet)
print(c)

#plt.scatter(dataSet[:, 0], dataSet[:, 1], c=y, marker="o", cmap='plasma')
scatter = plt.scatter([row[0] for row in dataSet], [row[1] for row in dataSet],c=c, label="data",cmap="plasma")
colorbar = plt.colorbar(scatter, label='data')
plt.xlabel('Axe X')
plt.ylabel('Axe Y')

# Ajout d'une légende
plt.legend()
plt.show()
