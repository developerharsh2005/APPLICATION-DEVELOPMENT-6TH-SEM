#19
def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//hcf(a,b)
a,b=map(int,input().split())
print(hcf(a,b),lcm(a,b))
