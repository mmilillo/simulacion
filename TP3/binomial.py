import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


#bernulli
def calcularBernoulli(p):
    if p < 0 or p > 100:
        return Exception

    num = np.random.random_sample() * 100 

    if num <= p: 
        return 1
    else:
        return 0

### DISTRIBUCION BINOMIAL ###

def calcularBinomial(n,p):
    exitos = 0
    for i in range(0, n):
        exitos = exitos + calcularBernoulli(p)
    
    return exitos
                    

resultados = np.zeros((100000),dtype=int)

for x in range(0, resultados.size):
    resultados[x] = calcularBinomial(20,60)

print(resultados)    



num_bins = 50
n, bins, patches = plt.hist(resultados, num_bins, facecolor='blue', alpha=0.5)
plt.show()
