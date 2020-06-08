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
#resultados[x] = calcularHipergeometrica(100,10,45)
def calcularHipergeometrica(poblacion,muestra,p):
    posiblesExito = (poblacion /100) * p # 10
    exitos = 0

    for i in range(0, muestra):
        resultado = calcularBernoulli(p)
        poblacion = poblacion -1
        if(resultado == 1):
            posiblesExito = posiblesExito -1
            exitos = exitos +1        
        p = (posiblesExito / poblacion) * 100

    
    return exitos
        
                    

resultados = np.zeros((10000),dtype=int)

for x in range(0, resultados.size):
    resultados[x] = calcularHipergeometrica(50,10,20) 



num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()
