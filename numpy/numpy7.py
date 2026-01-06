import numpy as np
n = 5
a = np.ones((n, n))
a[1:-1, 1:-1] = 0
print(a)
