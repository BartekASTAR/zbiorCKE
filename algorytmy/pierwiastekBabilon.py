#Metoda babilońska to stary, sięgający starożytności sposób przybliżonego obliczania pierwiastka kwadratowego z danej liczby.

def sqrt_babilonska(S):
    x = S/2
    eps = 0.0001
    y = 0
    while x - y > eps:
        y = S/x
        x = (x + y) / 2
    return x
print(sqrt_babilonska(12.45))