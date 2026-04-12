def horner(a,n,x):
    res = a[0]
    for i in range(1,n+1):
        res = (res*x) + a[i]
    return res

n,x = map(int, input().split())
a = list(map(int, input().split()))
print(horner(a,n,x))

