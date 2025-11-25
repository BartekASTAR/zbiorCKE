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


k = int(input())
a,b=0,0

a = k // potega(10,dlugosc(k)//2)
b = k % potega(10,dlugosc(k)//2)

sum = a+b
print(sum)

#for i in range(dlugosc(k)):
#    cyfra = k % 10
#    if i <= dlugosc(k)//2:
#        b += cyfra * potega(10,i)
#    else:
#        a += cyfra * potega(10,i)
#    k = k//10
#
print(a, b)
