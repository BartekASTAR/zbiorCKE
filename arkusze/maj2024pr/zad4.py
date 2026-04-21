import math

with open("liczby.txt", "r") as f:
    pierwsze, liczby = [line.strip().split() for line in f.readlines()]
    pierwsze = list(map(int, pierwsze))
    liczby = list(map(int, liczby))

ans = open("wyniki4.txt", "w")

#4.1
counter = 0
for i in pierwsze:
    for j in liczby:
        if j % i == 0:
            counter +=1
            break
ans.write(f"4.1\n{counter}\n\n")

#4.2
posort = sorted(pierwsze, reverse=True)
ans.write(f"4.2\n{posort[100]}\n\n")

#4.3
def rozklad(n):
    k = 2
    czynniki = {}
    pierw = int(math.sqrt(n)) + 1
    while n > 0 and k < pierw:
        while n % k == 0:
            if k not in czynniki.keys():
                czynniki[k] = 1
            else:
                czynniki[k] += 1
            n //= k
        k += 1
    if n > 1:
        czynniki[n] = 1
    return czynniki

dost_czyn = {}
for i in pierwsze:
    if i not in dost_czyn.keys():
        dost_czyn[i] = 1
    else:
        dost_czyn[i] += 1

ans.write(f"4.3\n")
for i in liczby:
    czyn = rozklad(i)
    for k,v in czyn.items():
        if k in dost_czyn.keys() and dost_czyn[k] >= v:
            pass
        else:
            break
    else:
        ans.write(f"{i}\n")

#4.4
test = [1,2,3,4,5,6,7]
maks_avr, liczba_el, pierwsz_el = 0,0,0,
for i in range(50, len(pierwsze)+1):
    for j in range(0, len(pierwsze)-i+1):
        wyc = pierwsze[j:j+i]
        avr = sum(wyc) / i
        if avr > maks_avr:
            maks_avr = avr
            liczba_el = i
            pierwsz_el = wyc[0]
ans.write(f"\n\n4.4\n{maks_avr} {liczba_el} {pierwsz_el}")