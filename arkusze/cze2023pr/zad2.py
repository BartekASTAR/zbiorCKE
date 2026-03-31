#2.1
counter = 0
def czy_mnijeszy(n,s,k1,k2):
    global counter
    counter = 0
    n=n-1
    i = k1-1
    j = k2-1
    while i <= n and j<=n:
        counter += 1
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False

print("2.1")
print(czy_mnijeszy(len("aaaaaabb"), "aaaaaabb", 1,2 ), counter)

#2.2
print("\n\n2.2")
with open("slowa1.txt", "r") as s1:
    slowa1 = [line.strip() for line in s1.readlines()]
with open("slowa2.txt", "r") as s2:
    slowa2 = [line.strip() for line in s2.readlines()]
with open("slowa3.txt", "r") as s3:
    slowa3 = [line.strip() for line in s3.readlines()]

print(slowa1)
print(slowa2)

for slowa in [slowa1, slowa2, slowa3]:
    #print(int(slowa[0]), slowa[1], int(slowa[2].split()[0]), int(slowa[2].split()[1]))
    if czy_mnijeszy(int(slowa[0]), slowa[1], int(slowa[2].split()[0]), int(slowa[2].split()[1])):
        print("TAK")
    else:
        print("NIE")

#2.3
print("\n\n2.3")
s = "mascarpone"
n = len(s)

tablica_suffixow = [s[i:] for i in range(n)]
indeksy_suffixow = [i+1 for i in range(n)]
print(tablica_suffixow)
print(indeksy_suffixow)
for i in range(n):
    for j in range(n-i-1):
        if not czy_mnijeszy(n,s,indeksy_suffixow[j],indeksy_suffixow[j + 1]):
            indeksy_suffixow[j], indeksy_suffixow[j + 1] = indeksy_suffixow[j + 1], indeksy_suffixow[j]
print(indeksy_suffixow)

#2.4
print("\n\n2.4")
with open("slowa4.txt", "r") as s4:
    slowa4 = [line.strip().split() for line in s4.readlines()]

for i in slowa4:
    s = i[1]
    n = len(s)
    tablica_suffixow = [s[i:] for i in range(n)]
    indeksy_suffixow = [i+1 for i in range(n)]
    #print(tablica_suffixow)
    #print(indeksy_suffixow)
    for i in range(n):
        for j in range(n-i-1):
            if not czy_mnijeszy(n,s,indeksy_suffixow[j],indeksy_suffixow[j + 1]):
                indeksy_suffixow[j], indeksy_suffixow[j + 1] = indeksy_suffixow[j + 1], indeksy_suffixow[j]
                tablica_suffixow[j], tablica_suffixow[j+1] = tablica_suffixow[j+1], tablica_suffixow[j]
    #print(indeksy_suffixow)
    print(tablica_suffixow[0])