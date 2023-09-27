import math
import random
import matplotlib.pyplot as plt
import numpy as np

def customFct(x):
    y = (x[0]*2.4 + x[1]*5.5)**2
    return round(y)

dataSet = []
c = []
dataSetLenght = 1000
max = customFct([10,10])



def fillData(d):
    for i in range(dataSetLenght):
        d.append([random.random()*10,random.random()*10])
        c.append(round(customFct(d[-1])/max))


fillData(dataSet)

#plt.scatter(dataSet[:, 0], dataSet[:, 1], c=y, marker="o", cmap='plasma')
scatter = plt.scatter([row[0] for row in dataSet], [row[1] for row in dataSet],c=c, label="data",cmap="plasma")
colorbar = plt.colorbar(scatter, label='data')
plt.xlabel('Axe X')
plt.ylabel('Axe Y')

# Ajout d'une légende
plt.legend()
plt.show()
