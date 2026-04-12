tekst = input()
wzorzec = input()
wl = len(wzorzec)
pozycje = []
for i in range(len(tekst)-wl+1):
    if tekst[i:i+wl] == wzorzec:
        pozycje.append(i+1)
for i in pozycje:
    print(i, end=" ")
if pozycje == []:
    print("BRAK")