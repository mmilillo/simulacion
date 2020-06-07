import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

### DISTRIBUCION UNIFORME ###

x = np.random.random_sample(10000000)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()





