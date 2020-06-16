import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as math

### DISTRIBUCION exponencial ###

def calcularExponencial(lan):
    num = np.random.random_sample()
    resultado = ( (- 1 / lan) * (math.log( 1 - num)))
    return resultado


### poisson

def calcularPoisson(x, lan):
    tiempo_maximo = 0
    ultimo_tiempo = 0
    for x in range(0, x):
        ultimo_tiempo = calcularExponencial(lan)
        if ultimo_tiempo > tiempo_maximo:
            tiempo_maximo = ultimo_tiempo
    
    return tiempo_maximo
    


resultados = np.zeros((10000),dtype=float)

lan = 2
param = 3

for x in range(0, resultados.size):
    resultados[x] = calcularPoisson(param, lan)

print(x)
num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()