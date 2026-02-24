#26
def calc(a):
    s=sum(a)
    avg=s/5
    sd=(sum((x-avg)**2 for x in a)/5)**0.5
    print(s,avg,sd)
nums=list(map(float,input().split()))
calc(nums)
