import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as math

### DISTRIBUCION exponencial ###

def calcularExponencial(lan):
    num = np.random.random_sample()
    resultado = ( (- 1 / lan) * (math.log( 1 - num)))
    return resultado

resultados = np.zeros((1000),dtype=float)

lan = 2

for x in range(0, resultados.size):
    resultados[x] = calcularExponencial(lan)

print(x)
num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()