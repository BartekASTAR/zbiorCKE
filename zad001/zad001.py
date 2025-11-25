counter = 0
def wynik(i):
    global counter
    if i < 3:
        counter += 1
        return 1
    else:
        if i%2 == 0:
            return wynik(i-3) +  wynik(i-1) + 1
        else:
            return wynik(i-1) %7

for i in [0,3,5,7,9,10]:
    counter = 0
    wynik(i)
    print(i, counter)

