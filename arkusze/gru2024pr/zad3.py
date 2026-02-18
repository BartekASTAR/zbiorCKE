with open("liczby.txt", "r") as f:
    file = [int(line.strip()) for line in f.readlines()]

ans = open("wyniki3.txt", "w")

#3.1
import math
counter = 0
first = 0
for i in file:
    if str(math.sqrt(i))[-2] == "." and str(math.sqrt(i))[-1] == "0":
        if counter == 0:
            first = i
        counter += 1
ans.write(f"3.1\nLiczba kwadratow: {counter}\nPirwszy kwadrat: {first}")

#3.2
def faktoryzacja(liczba):
    czynnik = 2
    dzielniki = set()
    while czynnik * czynnik <= liczba:
        while liczba % czynnik == 0:
            dzielniki.add(czynnik)
            liczba //= czynnik
        czynnik += 1
    if liczba > 1:
        dzielniki.add(liczba)
    return dzielniki

ans.write(f"\n3.2\n")
for i in file:
    if len(faktoryzacja(i)) >= 5:
        ans.write(f"{i}\n")

#3.3
rowne = []
wieksze, mniejsze,rown = 0,0,0
for i in file:
    min, max = "", ""
    for digit in sorted(str(i)):
        min+=digit
    for digit in sorted(str(i), reverse=True):
        max+=digit
    print(i, min, max)
    difference = int(max) - int(min)
    if difference > i:
        wieksze += 1
    elif difference < i:
        mniejsze += 1
    else:
        rown += 1
        rowne.append(i)
ans.write(f"\n\n6.3\nMniejsze: {mniejsze}\nWikeksze: {wieksze}\nRowne: {rown}\nLista rownych: {rowne}")