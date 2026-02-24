hundreds = int(input("Enter amount in hundreds: "))
amount = hundreds * 100
print("Total amount =", amount)

note100 = amount // 100
remaining = amount % 100

note50 = remaining // 50
remaining = remaining % 50

note10 = remaining // 10

print("100 Rupee notes:", note100)
print("50 Rupee notes :", note50)
print("10 Rupee notes :", note10)
