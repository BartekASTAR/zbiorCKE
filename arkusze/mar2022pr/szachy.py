with open("szachy.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]
    lista_szachow = []
    for i in range(0, len(file), 9):
        board = []
        for j in range(i, i+8):
            board.append(file[j])
        lista_szachow.append(board)
print(lista_szachow)

ans= open('wyniki1.txt', 'w')

#1.1
plansze_z_pustymi = 0
max_pustych = 0

for plansza in lista_szachow:
    czy_ma_pusta_kolumna = False
    obecnie_pustych = 0
    for kolumna in range(0,8):
        for wiersz in plansza:
            if wiersz[kolumna] != ".":
                break
        else:
            czy_ma_pusta_kolumna = True
            obecnie_pustych += 1
    if czy_ma_pusta_kolumna:
        plansze_z_pustymi += 1
        if obecnie_pustych > max_pustych:
            max_pustych = obecnie_pustych
ans.write(f"4.1\n{plansze_z_pustymi} {max_pustych}\n\n")

#1.2

rownowaga = 0
min_rownowaga = 64
for plansza in lista_szachow:
    lista_duze, lista_male = dict(), dict()
    for wiersz in plansza:
        for pole in wiersz:
            if pole.isupper():
                if pole not in lista_duze:
                    lista_duze[pole] = 1
                else:
                    lista_duze[pole] += 1
            elif pole.islower():
                if pole.upper() not in lista_male:
                    lista_male[pole.upper()] = 1
                else:
                    lista_male[pole.upper()] += 1
    if lista_male == lista_duze:
        rownowaga += 1
        if 2*sum(lista_duze.values()) < min_rownowaga:
            min_rownowaga = 2*sum(lista_duze.values())

ans.write(f"1.2\n{rownowaga} {min_rownowaga}\n\n")

#1.3
def czy_duzy(znak):
    if "A" <= znak <= "Z":
        return True
    else:
        return False

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

def czy_szachowany(wiersz, kolumna, krol, wieza):
    if wieza in wiersz and krol in wiersz:
        for width in range(2,9):
            for i in range(0, len(wiersz)-width+1):
                wycinek = wiersz[i:i+width]
                #print(wycinek)
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
                #print(wycinek)
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

K_szachowany, k_szachowany = 0,0
for plansza in lista_szachow:
    #K i w
    wiersz, kolumna = wiersz_kolumna(plansza, pozycja_krola(plansza, "K"))
    if czy_szachowany(wiersz, kolumna, "K", "w"):
        K_szachowany += 1
    #k i W
    wiersz, kolumna = wiersz_kolumna(plansza, pozycja_krola(plansza, "k"))
    if czy_szachowany(wiersz, kolumna, "k", "W"):
        k_szachowany += 1

ans.write(f"1.3\nCzarny szachowany: {k_szachowany}\nBialy szachowany: {K_szachowany}")

ans.close()
ans.close()