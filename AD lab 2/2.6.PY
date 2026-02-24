#6
m1=int(input())
m2=int(input())
m3=int(input())
t=m1+m2+m3
a=t/3
if a>=90:
    g="O"
elif a>=80:
    g="E"
elif a>=70:
    g="A"
elif a>=60:
    g="B"
elif a>=50:
    g="C"
else:
    g="F"
print(t,a,g)
