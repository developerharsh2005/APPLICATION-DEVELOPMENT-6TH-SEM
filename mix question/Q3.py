def sum_of_squares(n):
    if n == 0:
        return 0
    return (2 * n) ** 2 + sum_of_squares(n - 1)

n = int(input("Enter n: "))

even_numbers = [2 * i for i in range(1, n + 1)]
print("Even numbers used:", ", ".join(map(str, even_numbers)))

steps = []
for num in even_numbers:
    steps.append(f"{num}²")

print("Step by step calculation:", " + ".join(steps))
print("Sum of squares:", sum_of_squares(n))
