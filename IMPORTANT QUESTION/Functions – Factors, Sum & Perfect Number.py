def factor_info(n):
    factors = [i for i in range(1, n+1) if n % i == 0]
    return len(factors), sum(factors), sum(factors[:-1]) == n

num = int(input("Enter number: "))

count, total, perfect = factor_info(num)

print("Factors:", count)
print("Sum:", total)
print("Perfect Number:", "Yes" if perfect else "No")
