with open("prostokaty.txt", "r") as f:
    file = [list(map(int, line.strip().split())) for line in f.readlines()]

print(file)

ans = open("wyniki4.txt", "w")

#4.1
pola = []
for i in file:
    pola.append(i[0] * i[1])

ans.write(f"Min: {min(pola)}\nMax: {max(pola)}")

#4.2
max_ciag = 0
len_ciag = 0
last_ciag = 0
last_max_ciag = []
for i in range(len(file)):
    if len_ciag == 0:
        len_ciag += 1
        last_ciag = file[i]
        continue
    if file[i][0] <= file[i-1][0] and file[i][1] <= file[i-1][1]:
        len_ciag += 1
        last_ciag = file[i]
    else:
        if len_ciag > max_ciag:
            max_ciag = len_ciag
            last_max_ciag = last_ciag
        len_ciag = 0
ans.write(f"\n4.2\n{max_ciag+1} {last_max_ciag}")

#4.3
heights_dict = {}
for i in file:
    if i[0] in heights_dict.keys():
        heights_dict[i[0]].append(i[1])
    else:
        heights_dict[i[0]] = [i[1]]

for k,v in heights_dict.items():
    heights_dict[k].sort(reverse=True)

print(heights_dict)

pros2, pros3, pros5 = [],[],[]
for k,v in heights_dict.items():
    temp2,temp3,temp5 = 0,0,0
    for i in range(2):
        if len(v) >= i+1:
            temp2 += v[i]
    pros2.append(temp2)
    for i in range(3):
        if len(v) >= i + 1:
            temp3 += v[i]
    pros3.append(temp3)
    for i in range(5):
        if len(v) >= i + 1:
            temp5 += v[i]
    pros5.append(temp5)

ans.write(f"4.3\n2 prostokaty: {max(pros2)}\n3 prostokaty: {max(pros3)}\n5 prostokatow: {max(pros5)}")
