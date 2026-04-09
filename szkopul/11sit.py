import math
def sito(n):
    pierwsza = [1 for _ in range(1,n)]
    pierwsza = [0,0] + pierwsza

    for i in range(2,int(math.sqrt(n))+1):
        for j in range(i*i, n+1, i):
            pierwsza[j] = 0

    return pierwsza

n = int(input())
sito = sito(n)
counter = 0
if n < 2:
    print(0)
    print("BRAK")
else:
    for i in range(len(sito)):
        if sito[i] == 1:
            counter += 1
            max = i
    print(counter)
    print(max)
