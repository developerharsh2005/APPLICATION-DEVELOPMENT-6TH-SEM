#23
def bin(n):
    if n==0:
        return ""
    return bin(n//2)+str(n%2)
n=int(input())
print(bin(n) or "0")
