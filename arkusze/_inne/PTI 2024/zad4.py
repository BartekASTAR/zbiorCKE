with open("konta.txt", "r") as f:
    file = [line.strip().split() for line in f.readlines()]

print(file)

ans = open("wyniki4.txt", "w")

graf = dict()
for kto, kogo in file: #TODO: poprawić sprawdzanie fałszywych kont; z jakiegoś powodu są one zdublowane
    if kto not in graf.keys():
        graf[kto] = [kogo]
    else:
        graf[kto].append(kogo)
    if kogo not in graf.keys():
        graf[kogo] = []

print(graf)

#4.1
ans.write(f"4.1\n{len(graf.keys())}\n\n")

#4.2
falszywe = []
for k,v in graf.items():
    for i in graf.values():
        if k in i:
            break
    else:
        if k not in falszywe:
            falszywe.append(k)


        falszywe.append(k)
ans.write(f"4.2\n{len(falszywe)} {falszywe}\n\n")

#4.3
pary = []
for k,v in graf.items():
    for i in v:
        if k in graf[i] and [k, i] not in pary:
            pary.append([k, i])
ans.write(f"4.3\n{int(len(pary)/2)}\n\n")

#4.4
konto = ""
najwiecej = 0
for k,v in graf.items():
    if len(v) > najwiecej:
        najwiecej = len(v)
        konto = k

ans.write(f"4.4\n{konto}\n\n")

#4.5
graf_obserwujacy = dict()
for users in graf.keys():
    graf_obserwujacy[users] = []
for k, v in graf.items():
    for i in v:
        graf_obserwujacy[i].append(k)

max_obserwujacych = 0
kto_max = ""
for k,v in graf_obserwujacy.items():
    liczba_nie_falsz = 0
    for i in v:
        if i not in falszywe:
            liczba_nie_falsz +=1
    if liczba_nie_falsz > max_obserwujacych:
        max_obserwujacych = liczba_nie_falsz
        kto_max = k
ans.write(f"4.5\n{kto_max}")



