

P = float(input("Enter Principal Amount (P): "))
T = float(input("Enter Time in years (T): "))
R = float(input("Enter Rate of Interest (R): "))

A = P * (1 + R/100) ** T
CI = A - P

print("Compound Interest =", CI)
print("Total Amount =", A)
