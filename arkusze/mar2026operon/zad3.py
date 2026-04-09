import math

with open("pociagi.txt", "r") as f:
    file = [list(map(int, line.strip().split())) for line in f.readlines()]
    print(file)
ans = open("wyniki3.txt", "w")

#3.1
nosnosc_pierwsza, nosnosc_41 =0,0
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in file:
    if isPrime(i[1]):
        nosnosc_pierwsza += 1
    if i[1] == 41:
        nosnosc_41 += 1
ans.write(f"3.1\nLiczba wagonow pierwszych: {nosnosc_pierwsza}\nLiczba wagonow o wadze 41: {nosnosc_41}\n\n")

#3.2
sklad = {}
for numer, waga in file:
    if numer not in sklad.keys():
        sklad[numer] = [1,waga]
    else:
        sklad[numer][0] += 1
        sklad[numer][1] += waga

max_dlugosc = 0
max_numer = 0
max_nosnosc = 0
for k,v in sklad.items():
    if v[0] > max_dlugosc:
        max_dlugosc = v[0]
        max_numer = k
        max_nosnosc = v[1]
ans.write(f"3.2\nNumer najdluzszego pociagu: {max_numer}\nDlugosc pociagu: {max_dlugosc}\nSuma wag wagonow: {max_nosnosc}\n\n")

#3.3
sklad2 = {}
for numer, waga in file:
    if numer not in sklad2.keys():
        wagony = {waga:1}
        sklad2[numer] = wagony
    else:
        if waga not in sklad2[numer].keys():
            sklad2[numer][waga] = 1
        else:
            sklad2[numer][waga] += 1

print(sklad2)
max_numer, max_liczba, max_nosnosc = 0,0,0
for k,v in sklad2.items():
    max_k, max_v = 0,0
    for k2,v2 in v.items():
        if v2 > max_v:
            max_v = v2
            max_k = k2
    if max_v > max_liczba:
        max_liczba = max_v
        max_numer = k
        max_nosnosc = max_k
ans.write(f"3.3\nNumer pociagu: {max_numer}\nNajczestsza nosnosc: {max_nosnosc}\nLiczba max nosnosc: {max_liczba}")
