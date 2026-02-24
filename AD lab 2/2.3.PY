#3
y=int(input())
if (y%400==0) or (y%4==0 and y%100!=0):
    print("Leap Year")
else:
    print("Not Leap Year")
