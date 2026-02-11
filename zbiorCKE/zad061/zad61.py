with open("ciagi.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

    ciagi = []
    for i in range(len(file)):
        if i % 2 == 0:
            continue
        else:
            ciagi.append(list(map(int,file[i].split())))
    print(ciagi)

ans = open("wyniki61.txt", "w")

#61.1
r_max = 0
r_counter = 0
def czy_arytmetyczny(ciag):
    global r_counter
    global r_max
    r_temp = 0
    r = ciag[1] - ciag[0]
    for i in range(1,len(ciag)-1):
        r_temp = ciag[i + 1] - ciag[i]
        if r_temp != r:
            break
    else:
        r_counter += 1
        if r > r_max:
            r_max = r

for i in ciagi:
    czy_arytmetyczny(i)
ans.write(f"61.1\nIlosc ciagow arytmetycznych: {r_counter}\nNajwieksza roznica: {r_max}\n\n")

#61.2
import math
ans.write(f"6.2\n")
for i in ciagi:
    sze_max = 0
    for j in i:
        for k in range(1, int(math.sqrt(j))+1):
            if k*k*k > j:
                break
            elif k*k*k == j and k*k*k > sze_max:
                sze_max = k*k*k
                break
    if sze_max > 0:
        ans.write(f"{sze_max}\n")

#61.3

with open("bledne.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

    ciagi = []
    for i in range(len(file)):
        if i % 2 == 0:
            continue
        else:
            ciagi.append(list(map(int,file[i].split())))
    print(ciagi)

def znajdz_blad(ciag):
    wyrazy = set()
    roz_list = []
    for i in range(0,len(ciag)-1):
        r = ciag[i + 1] - ciag[i]
        roz_list.append(r)
        wyrazy.add(r)
    roznice = {}
    for i in wyrazy:
        roznice[i] = 0
    for i in range(0,len(ciag)-1):
        r = ciag[i + 1] - ciag[i]
        roznice[r] += 1
    k_max, v_max = 0,0
    for k,v in roznice.items():
        if v > v_max:
            k_max = k
            v_max = v
    if roz_list[0] != k_max and roz_list[1] == k_max:
        return ciag[0]
    if roz_list[-1] != k_max and roz_list[-2] == k_max:
        return ciag[-1]
    for i in range(len(roz_list)-1):
        if roz_list[i] != k_max and roz_list[i+1] != k_max:
            return ciag[i+1]



ans.write(f"\n61.3\n")
for i in ciagi:
    ans.write(str(znajdz_blad(i)))
    ans.write("\n")













