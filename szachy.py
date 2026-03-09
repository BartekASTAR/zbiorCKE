#szachy 2
#plik= open('szachy.txt', 'r')
#zapis= open('zadanie1_2.txt', 'w')
#lista_szachow = []
#licznik_rownowagi = 0
#najmniejsza = 10
#def czy_duzy(znak):
#    if "A" <= znak <= "Z":
#        return True
#    else:
#        return False
#
#for i in range(125):
#    macierz = []
#    while True:
#        linia = plik.readline().strip()
#        if linia != "":
#            macierz.append(list(linia))
#        else:
#            break
#    lista_szachow.append(macierz)
#def rownowaga(macierz):
#    slownik_malych = {}
#    slownik_duzych = {}
#    czy_rownowaga = False
#    for i in range(len(macierz)):
#        for j in range(len(macierz)):
#            if macierz[i][j] != ".":
#                if czy_duzy(macierz[i][j]):
#                    if macierz[i][j] not in slownik_duzych:
#                        slownik_duzych[macierz[i][j].lower()] = 1
#                    else:
#                        slownik_duzych[macierz[i][j].lower()] += 1
#                else:
#                    if macierz[i][j] not in slownik_malych:
#                        slownik_malych[macierz[i][j]] = 1
#                    else:
#                        slownik_malych[macierz[i][j]] += 1
#    if slownik_duzych == slownik_malych:
#        return [slownik_malych,slownik_duzych]
#    else:
#        return False
#for macierz in lista_szachow:
#    if rownowaga(macierz) != False:
#        licznik_rownowagi += 1
#        slowniki = rownowaga(macierz)
#        if len(slowniki[0]) < najmniejsza:
#            najmniejsza = len(slowniki[0]) * 2
#zapis.write(f"{licznik_rownowagi} ")
#zapis.write(f"{najmniejsza}")
#zapis.close()
#plik.close()
from operator import index

#szachy 3
plik= open('szachy.txt', 'r')
zapis= open('zadanie1_2.txt', 'w')
lista_szachow = []
licznik_rownowagi = 0
najmniejsza = 10
def czy_duzy(znak):
    if "A" <= znak <= "Z":
        return True
    else:
        return False

for i in range(125): #zmienic na 125 przy normalnym pliku
    macierz = []
    while True:
        linia = plik.readline().strip()
        if linia != "":
            macierz.append(list(linia))
        else:
            break
    lista_szachow.append(macierz)

def pozycja_krola(macierz, krol):
    for x in range(8):
        for y in range(8):
            if macierz[x][y] == krol:
                return (x, y)

def pozycja_wiezy(macierz, wieza):
    pozycje = []
    for x in range(8):
        for y in range(8):
            if macierz[x][y] == wieza:
                pozycje.append((x, y))
    return pozycje

def wiersz_kolumna(macierz, poz_krola):
    wiersz = macierz[poz_krola[0]]
    kolumna = []
    for x in range(8):
        kolumna.append(macierz[x][poz_krola[1]])
    return wiersz, kolumna

def czy_szachowany(macierz, wiersz, kolumna, krol, wieza):
    if wieza in wiersz and krol in wiersz:
        #pomysl1: wersja z sprawdzaniem ranga od wiezy do króla lub od króla do wiezy czy są same kropki po drodze
        #for i in range(wiersz):
        #    if wiersz[i] == krol:
        #        poz_krola = i
        #    if wiersz[i] == wieza:
        #        wieze.append(i)
        #for poz_wieza in wieze:
        #    if poz_wieza < poz_krola:
        #        for i in range(poz_wieza+1, poz_krola):
        for width in range(2,9):
            for i in range(0, len(wiersz)-width+1):
                wycinek = wiersz[i:i+width]
                print(wycinek)
                if wieza in wycinek and krol in wycinek:
                    for j in range(1, len(wycinek)-1):
                        if wycinek[j] != ".":
                            break
                    else:
                        return True


    if wieza in kolumna and krol in kolumna:
        for width in range(2, 9):
            for i in range(0, len(kolumna) - width + 1):
                wycinek = kolumna[i:i + width]
                print(wycinek)
                if wieza in wycinek and krol in wycinek:
                    for j in range(1, len(wycinek) - 1):
                        if wycinek[j] != ".":
                            break
                    else:
                        return True
    return False


def print_plansza(macierz):
    for x in range(8):
        for y in range(8):
            print(macierz[x][y], end="")
        print()

#for plansza in lista_szachow:
#print(lista_szachow)
#plansza = lista_szachow[0]
#print_plansza(plansza)
#
#print("(Y, X)")
#print(pozycja_krola(plansza, "K"))
#wiersz, kolumna = wiersz_kolumna(plansza, pozycja_krola(plansza, "K"))
#print(wiersz)
#print(kolumna)
#
#wiersz = [".",".",".","w",".",".","K","."]
#
#czy_szachuje(plansza, wiersz,kolumna,"K", "w")

K_szachowany, k_szachowany = 0,0
for plansza in lista_szachow:
    #K i w
    wiersz, kolumna = wiersz_kolumna(plansza, pozycja_krola(plansza, "K"))
    if czy_szachowany(plansza, wiersz, kolumna, "K", "w"):
        K_szachowany += 1
    #k i W
    wiersz, kolumna = wiersz_kolumna(plansza, pozycja_krola(plansza, "k"))
    if czy_szachowany(plansza, wiersz, kolumna, "k", "W"):
        k_szachowany += 1

print(f"Czarny szachowany: {k_szachowany}\nBiały szachowany: {K_szachowany}")

zapis.write(f"{licznik_rownowagi} ")
zapis.write(f"{najmniejsza}")
zapis.close()
plik.close()