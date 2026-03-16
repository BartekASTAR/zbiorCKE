import math

from fontTools.afmLib import readlines

def potmod(a,x,m):
    return szybkaPotega(a,x) % m

#print(potmod(3,3,11))
#
#
#for i in range(1000):
#    if (math.pow(2,i)-5) % 59 == 0:
#        print(i)
#        break
#
#print(potmod(9,2,80))

ans = open("wyniki3.txt", "w")

ans.write(f"3.1\n5\n5\n6\n1\n\n")

#3.2

def potega(a,x):
    liczba = 1
    for i in range(x):
        liczba = liczba*a
    return liczba

def szybkaPotega(a,x):
    if x == 0:
        return 1
    if x == 1:
        return a
    if x % 2 == 0:
        polowa = szybkaPotega(a,x//2)
        return polowa*polowa
    else:
        return a * szybkaPotega(a,x-1)

#3.3
with open("liczby.txt", "r") as f:
    file = [list(map(int, line.strip().split())) for line in f.readlines()]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

counter = 0
for i in file:
    if isPrime(i[0]):
        counter += 1

ans.write(f"3.3\n{counter}\n\n")

#3.4
counter = 0
for i in file:
    if math.gcd(i[0], i[1]) == 1:
        counter +=1
ans.write(f"3.4\n{counter}\n\n")

#3.5
counter = 0
for i in file:
    reszty = set()
    for x in range(i[0]):
        if x == 0:
            r = 1
            continue
        r = r*i[1] % i[0]
        if r == i[2]:
            counter += 1
            break
        elif r in reszty:
            break
        else:
            reszty.add(r)




ans.write(f"3.5\n{counter}\n\n")