with open("przyklad.txt", "r") as f:
    file = [int(line.strip()) for line in f.readlines()]

ans = open("wyniki3.txt", "w")

print(file)

import math
#3.1
counter = 0
for a in range(len(file)-1):
    if math.gcd(file[a], file[a+1]) == 1:
        counter += 1
ans.write(f"3.1\n{counter}\n\n")

#3.2
counter = 0
trojki = []
for i in range(len(file)-2):
    a,b,c = file[i], file[i+1], file[i+2]
    if a + b == c and len(str(a)) < len(str(b)) and len(str(b)) < len(str(c)):
        counter += 1
        trojki.append([a,b,c])
ans.write(f"3.2\n{counter}\n")
for i in trojki:
    ans.write(f"{i[0]} {i[1]} {i[2]}")

#3.3
