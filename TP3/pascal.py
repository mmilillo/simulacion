import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def calcularBernoulli(p):
    if p < 0 or p > 100:
        return Exception

    num = np.random.random_sample() * 100 

    if num <= p: 
        return 1
    else:
        return 0

### DISTRIBUCION GEOMETRICA ###

def calcularPascal(n,p,intentos,exitos):
    intentos = intentos +1
    exitos = exitos + calcularBernoulli(p)

    if exitos == n:
        return intentos
    else:
        return calcularPascal(n,p,intentos,exitos)
                    

resultados = np.zeros((100000),dtype=int)

for x in range(0, resultados.size):
    resultados[x] = calcularPascal(10,50,0,0)

print(resultados)    



num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()
