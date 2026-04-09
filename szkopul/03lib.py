n = int(input())
liczby = []
for _ in range(n):
    i = int(input())
    liczby.append(i)

for i in liczby:
    binarna = ""
    while i > 0:
        print(f"{i} / 2 = {i//2} reszta {i%2}")
        binarna = str(i%2) + binarna
        i //=2
    print(f"Binarna: {binarna}")
    print(f"Jedynki: {list(binarna).count("1")}")
    if list(binarna).count("1") == 1:
        print(f"Potega2: TAK\n")
    else:
        print(f"Potega2: NIE\n")