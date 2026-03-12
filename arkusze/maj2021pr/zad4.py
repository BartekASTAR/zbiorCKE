with open("instrukcje.txt", "r") as f:
    file = [line.strip().split() for line in f.readlines()]

print(file)

napis = []

def zmiana_litery(litera):
    liczba = ord(litera)
    if liczba == 90:
        return chr(65)
    else:
        return chr(liczba+1)


for i in file:
    if i[0] == "DOPISZ":
        napis.append(i[1])
    elif i[0] == "USUN":
        for j in range(int(i[1])):
            napis.pop()
    elif i[0] == "ZMIEN":
        napis.pop()
        napis.append(i[1])
    elif i[0] == "PRZESUN":
        for ind, j in enumerate(napis):
            if j == i[1]:
                napis[ind] = zmiana_litery(napis[ind])
                break

napis  = "".join(napis)
print(napis)

ans = open("wyniki4.txt", "w")

#4.1
ans.write(f"4.1\n{len(napis)}\n\n")

#4.2
obecna = ""
max_wyst, obec_wyst = 0,0
max_inst = ""
for ind, instrukcja in enumerate(file):
    if ind == 0:
        obecna = instrukcja[0]
        obec_wyst = 1
    if instrukcja[0] != obecna:
        if obec_wyst > max_wyst:
            max_wyst = obec_wyst
            max_inst = obecna
        obecna = instrukcja[0]
        obec_wyst = 1
    else:
        obec_wyst +=1

ans.write(f"4.2\n{max_inst} {max_wyst}\n\n")

#4.3
litery = dict()
for instrukcja, parametr in file:
    if instrukcja=="DOPISZ":
        if parametr not in litery.keys():
            litery[parametr] = 1
        else:
            litery[parametr] += 1

max_wystapien = max(litery.values())

for k,v in litery.items():
    if v == max_wystapien:
        ans.write(f"4.3\n{k} {max_wystapien}\n\n")

#4.4
ans.write(f"4.4\n{napis}")

