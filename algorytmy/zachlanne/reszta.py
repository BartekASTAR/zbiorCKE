def reszta(kwota):
    nominal = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    ile_nominalow = [0 for i in range(9)]
    i = 0
    while kwota > 0:
        x = kwota // nominal[i]
        ile_nominalow[i] = x
        kwota -= x * nominal[i]
    return ile_nominalow

def reszta_slownik(kwota):
    ile_nominalow = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    for nominal in ile_nominalow.keys():
        if kwota <= 0:
            break
        x = kwota // nominal
        ile_nominalow[nominal] = x
        kwota -= x * nominal
    return ile_nominalow