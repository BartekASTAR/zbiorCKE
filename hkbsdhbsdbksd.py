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
z
print(czyNudna(229))


