#zad 2.3
#ułamek to będzie lista dwuelementowa [licznik, mianowanik]
import math

def fareyN(n):
    farey = [[0, 1], [1, 1]]
    czyDodanoElement = True
    while czyDodanoElement:
        czyDodanoElement = False
        new_farey = farey
        for i in range(len(farey)-1):
            new_item = [farey[i][0]+farey[i+1][0], farey[i][1]+farey[i+1][1]]
            dzielnik = math.gcd(new_item[0], new_item[1])
            new_item = [new_item[0]//dzielnik, new_item[1]//dzielnik] #  forma nieskracalna ulamka
            if new_item[1] > n:
                continue
            else:
                czyDodanoElement = True
                new_farey.insert(i+1, new_item)
        farey = new_farey
    return farey
#2.4
an = [0]
for i in range(1,11):
    an.append(len(fareyN(i)))

print(f"2.4 {len(fareyN(16))}")
