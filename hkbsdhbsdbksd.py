def sumaKwCyfr(n):
    dlc = 0
    while n > 0:
        c = n % 10
        dlc += c*c
        n = n//10
    return dlc


tab = [0 for i in range(244)]

def czyNudna(n):
    global tab
    wynik = sumaKwCyfr(n)
    if wynik == 1:
        return True
    if tab[wynik] == 1:
        return False
    tab[wynik] = 1
    return czyNudna(wynik)


import math

#ZAD zbCKE 20
def narcyz(x, xB):
    sum = 0
    for i in range(len(str(xB))):
        sum += math.pow(int(str(xB)[i]), len(str(xB)))
    return sum


def Bnarcyz(xB,B):
    sum = 0
    for i in range(len(str(xB))):
        sum += int(str(xB)[i]) * math.pow(B,len(str(xB))-i-1)
    return sum


print(Bnarcyz(11101111110001,2))
print(narcyz(15345,11101111110001))
