n = int(input("Enter n: "))

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

result = []
count_both = 0

for i in range(1, n+1):
    p = is_palindrome(i)
    a = is_armstrong(i)
    if p or a:
        result.append(i)
    if p and a:
        count_both += 1

print("Palindrome or Armstrong Numbers:", *result)
print("Count satisfying both:", count_both)
