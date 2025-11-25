import math

with open("liczby2.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

def dlugosc(liczba):
    n = 0
    while liczba > 0:
        n += 1
        liczba = liczba// 10
    return n

def potega(n,k):
    if k == 0:
        return 1
    wynik = n
    for i in range(int(k)-1):
        wynik *= n
    return wynik


lista_kaperkar = []
for i in file:
    kaperkar = 0
    i_sqr = int(i)**2
    for j in range(1,len(str(i_sqr))):
        a = int(i_sqr) // potega(10, j)
        b = int(i_sqr) % potega(10, j)
        if a + b <= int(i):
            kaperkar += 1
    lista_kaperkar.append(kaperkar)

print(max(lista_kaperkar))
print(file[lista_kaperkar.index(max(lista_kaperkar))])
