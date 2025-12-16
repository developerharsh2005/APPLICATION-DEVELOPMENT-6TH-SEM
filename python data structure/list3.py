lst = list(map(int, input("Enter list elements: ").split()))
count = 0

for num in lst:
    if num % 2 == 0:
        count += 1

print("Number of even elements =", count)
