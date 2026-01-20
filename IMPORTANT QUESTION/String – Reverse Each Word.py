sentence = input("Enter sentence: ")

words = sentence.split()
result = []

for word in words:
    clean = ''.join(c for c in word if c.isalnum())
    result.append(clean[::-1])

print(" ".join(result))
