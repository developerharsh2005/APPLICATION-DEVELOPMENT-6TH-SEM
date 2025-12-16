n = int(input("Enter number of elements: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

max_key = max(d, key=d.get)

print("Dictionary:", d)
print("Key with maximum value =", max_key)
