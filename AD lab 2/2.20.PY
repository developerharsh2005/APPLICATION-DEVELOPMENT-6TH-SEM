#20
def s(n):
    if n==0: return 0
    return n+s(n-1)
print(s(int(input())))
