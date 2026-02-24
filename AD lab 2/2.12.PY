#12
n=int(input())
p=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        p=False
        break
print("Prime" if p and n>1 else "Not Prime")
