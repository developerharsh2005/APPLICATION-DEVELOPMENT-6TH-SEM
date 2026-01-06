import numpy as np
a = np.random.rand(10, 10)
blocks = []
for i in range(8):
    for j in range(8):
        blocks.append(a[i:i+3, j:j+3])
print(np.array(blocks))
