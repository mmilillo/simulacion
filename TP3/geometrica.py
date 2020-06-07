import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

### DISTRIBUCION GEOMETRICA ###

def geometrica():
    return calcularBernoulli()

def calcularBernoulli():
    num = np.random.random_sample() * 10
    if num > 5:
        return 1
    else:
        return calcularBernoulli() + 1
                    

resultados = np.zeros((10000),dtype=int)

for x in range(0, resultados.size):
    resultados[x] = geometrica()

x = resultados
print(x)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
