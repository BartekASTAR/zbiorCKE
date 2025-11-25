import math

with open("liczby1.txt", "r") as f:
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
    for i in range(k-1):
        wynik *= n
    return wynik


counter = 0
for i in file:
    a = int(i) // potega(10, dlugosc(int(i)) // 2)
    b = int(i) % potega(10, dlugosc(int(i)) // 2)
    if math.gcd(a,b) == 1:
        counter += 1
print(counter)
