import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

matrix = np.random.randint(1, 101, (4, 4))
print("Original Matrix:")
print(matrix)

primes = [x for x in matrix.flatten() if is_prime(x)]
print("Prime Numbers Found:", primes)

modified = matrix.copy()
for i in range(4):
    for j in range(4):
        if is_prime(modified[i][j]):
            modified[i][j] = -1

print("Modified Matrix:")
print(modified)

non_primes = modified[modified != -1]
average = non_primes.mean()
print("Average of non-prime numbers:", round(average, 2))
