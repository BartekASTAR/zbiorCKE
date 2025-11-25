#Algorytm euklidesa służy do znajdywania NWD

def gcd(a, b):
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(gcd(18, 12))