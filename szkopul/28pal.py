n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i in words:
    zmiany = 0
    po_zmianie = list(i)
    isPalindorm = True
    for l in range(len(i)//2):
        if i[l] == i[-l-1]:
            print(f"{i[l]} == {i[-l-1]}? TAK")
        else:
            isPalindorm = False
            zmiany += 1
            po_zmianie[-l-1] = po_zmianie[l]
            print(f"{i[l]} == {i[-l-1]}? NIE")
    if isPalindorm:
        print("Palindrom: TAK\n")
    else:
        print("Palindrom: NIE")
        print(f"Zmiany: {zmiany}")
        print(f"Wynik: {"".join(po_zmianie)}\n")