with open("liczby.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

ans = open("wyniki59.txt", "w")

import math
def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

#59.1
counter = 0
dividors = []
for i in file:
    n = int(i)
    d=3
    div = set()
    if n % 2 == 0:
        continue
    while d*d <= n:
        if n % d == 0:
            div.add(d)
            while n % d == 0:
                n = n // d
            if len(div) > 3:
                break
        d+=2
    if n >1:
        div.add(n)
    if len(div) == 3:
        counter += 1
print(counter)
ans.write(f"59.1\n{counter}\n")

#59.2
counter = 0
for i in file:
    suma = int(i) + int(i[::-1])
    if str(suma) == str(suma)[::-1]:
        counter += 1
ans.write(f"59.2\n{counter}\n")
print(counter)

#59.3
def ilocz_cyfr(n):
    ilocz = 1
    for i in str(n):
        ilocz *= int(i)
    return ilocz
moc = [0] * 10
for i in file:
    k = 0
    n = int(i)
    while n > 9:
        n = ilocz_cyfr(n)
        k+=1
    moc[k] += 1

ans.write(f"59.3")
print(moc)
for i in range(1,9):
    ans.write(f"{i} {moc[i]}\n")
    print(f"{i} {moc[i]}")

ans.close()