import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

### DISTRIBUCION UNIFORME ###

def calcularBernoulli(p):
    if p < 0 or p > 100:
        return Exception

    num = np.random.random_sample() * 100 

    if num <= p: 
        return 1
    else:
        return 0

resultados = np.zeros((10000),dtype=int)

p = 30

for x in range(0, resultados.size):
    resultados[x] = calcularBernoulli(p)

print(x)
num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()