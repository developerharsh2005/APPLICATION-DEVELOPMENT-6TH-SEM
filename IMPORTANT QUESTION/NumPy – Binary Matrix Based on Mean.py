import numpy as np

matrix = np.random.randint(1, 100, (5, 5))
mean = matrix.mean()

binary = np.where(matrix > mean, 1, 0)

print("Random Matrix:\n", matrix)
print("Binary Matrix based on Mean:\n", binary)
