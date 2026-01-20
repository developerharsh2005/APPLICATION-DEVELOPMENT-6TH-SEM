def count_zeros(n):
    if n == 0:
        return 0
    return (1 if n % 10 == 0 else 0) + count_zeros(n // 10)

num = int(input("Enter number: "))
print("Number of zeros =", count_zeros(num))
