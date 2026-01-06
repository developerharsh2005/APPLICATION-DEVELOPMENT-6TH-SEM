import numpy as np
m = np.zeros((4, 4), dtype=int)
m[np.arange(3), np.arange(1, 4)] = [1, 2, 3]
m[np.arange(1, 4), np.arange(3)] = [1, 2, 3]
print(m)
