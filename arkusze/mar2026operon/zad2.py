#2.3
def bin2dec(bin):
    dec = 0
    bit = 8
    for i in range(0,4):
        dec = dec + int(bin[i])*bit
        bit = bit//2
    return dec

with open("zegar_binarny.txt") as f:
    zegary = [line.strip().split() for line in f.readlines()]
    print(zegary)

ans = open("wyniki2.txt", "w")

#2.4
def zegar_godzina(zegar):
    wynik = ""
    for i in zegar:
        wynik += str(bin2dec(i))
    return wynik

counter = 0
indeksy = []
for i in range(len(zegary)):
    if zegar_godzina(zegary[i]) == "172214":
        counter += 1
        indeksy.append(i+1)
ans.write(f"2.3\n{counter}\n{indeksy}")

#2.5
ans.write(f"\n\n2.4\n")
for i in zegary:
    if i[2] != "0000" and i[4] != "0000":
        if  i[2] == i[4] and i[3] == i[5]:
            for j in range(6):
                ans.write(f"{i[j]} ")
                if j == 5:
                    ans.write("\n")


