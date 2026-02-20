import numpy as np

nola = np.arange(start = 1, stop = 65, step = 2).reshape((4,8))
nola = nola[:,:-1]
print(nola)