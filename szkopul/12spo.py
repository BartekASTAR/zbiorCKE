def pow(a,b,m):
    if b == 0:
        return 1
    elif b % 2 == 0:
        squared = pow(a, b//2,m)
        return (squared * squared) % m
    else:
        return (a * pow(a, b-1,m)) % m

a,b,m = list(map(int, input().split()))
print(pow(a,b,m))