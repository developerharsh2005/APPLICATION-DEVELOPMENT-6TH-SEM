import numpy as np
v = np.random.rand(10)
v[:5] = np.sort(v[:5])
v[5:] = np.sort(v[5:])[::-1]
print(v)
