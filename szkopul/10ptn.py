def ptn(a,n):
    res = 1
    M = 1000000007
    for i in range(n):
        res = (res*a)%M
    return res

a,n = list(map(int, input().split()))
print(ptn(a,n))