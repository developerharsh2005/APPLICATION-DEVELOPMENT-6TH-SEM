t = tuple(map(int, input("Enter tuple elements: ").split()))
key = int(input("Enter element to search: "))

if key in t:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")
