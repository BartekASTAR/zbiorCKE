import math

n = int(input())

sito = [1] * (n+1)
sito[0], sito[1] =0, 0

for i in range(2, int(math.sqrt(n) + 1)):
    if sito[i] == 1:
        for j in range(i*i, n+1, i):
            sito[j] = 0
print(sito)
