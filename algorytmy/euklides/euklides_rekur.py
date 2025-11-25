def gcd(a,b):
    if b == 0:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return  gcd(a, b - a)

print(gcd(12, 24))
