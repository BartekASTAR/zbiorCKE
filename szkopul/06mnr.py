n = int(input())

def mrch(a,b):
    wynik = 0
    while b != 0:
        if b % 2 == 1:
            print(f"{a} {b} DODAJ")
            wynik += a
        else:
            print(f"{a} {b} POMIN")
        a += a
        b //= 2
    print(f"Wynik: {wynik}\n")


a_b = []
for _ in range(n):
    a_b.append(list(map(int, input().split())))
for i in a_b:
    a,b = i
    mrch(a,b)