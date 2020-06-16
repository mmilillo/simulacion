import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as math

### DISTRIBUCION exponencial ###
## tiempo que falta hasta proximo cliente
def calcularExponencial(lan):
    num = np.random.random_sample()
    resultado = ( (- 1 / lan) * (math.log( 1 - num)))
    return resultado


### poisson
## cantidad de personas en una unidad
def calcularPoisson(lan):
    tiempo_transcurrido = 0
    cantidad = 0

    while tiempo_transcurrido < lan:
        tiempo_transcurrido = tiempo_transcurrido + calcularExponencial(lan)
        if tiempo_transcurrido < lan:
            cantidad = cantidad +1
    
    return cantidad
    


resultados = np.zeros((100000),dtype=float)

lan = 5

for x in range(0, resultados.size):
    resultados[x] = calcularPoisson(lan)

print(x)
num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()