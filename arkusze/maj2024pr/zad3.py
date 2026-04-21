# 3.1
import math


def skrot(n):
    m = 0
    mnoz = 1
    while n>0:
        t = n % 10
        if t % 2 != 0:
            m += t * mnoz
            mnoz *= 10
        n = n//10
    return m
#print(skrot(123456))

def wszParz(n):
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 != 0:
            break
    else:
        return True
    return False

#3.2
with open("skrot.txt", "r") as f:
    file = [int(line.strip()) for line in f.readlines()]

ans = open("wyniki3.txt", "w")

counter = 0
maks_parz = 0
for i in file:
    if wszParz(i):
        counter += 1
        if i > maks_parz:
            maks_parz = i

ans.write(f"3.2\n{counter}\n{maks_parz}\n\n")


#3.3
ans.write(f"3.3\n")
from math import gcd
with open("skrot2.txt", "r") as f:
    file = [int(line.strip()) for line in f.readlines()]
for i in file:
    skrt = skrot(i)
    if math.gcd(i, skrt) == 7:
        ans.write(f"{i}\n")