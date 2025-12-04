with open("dane_systemy1.txt", "r") as f1:
    dane1 = [line.strip().split() for line in f1]
with open("dane_systemy2.txt", "r") as f2:
    dane2 = [line.strip().split() for line in f2]
with open("dane_systemy3.txt", "r") as f3:
    dane3 = [line.strip().split() for line in f3]

ans = open("wyniki058.txt", "w")

#58.1
temp1,temp2,temp3 = [],[],[]
time1, time2, time3 = [],[],[]
for i in dane1:
    temp1.append(int(i[1], 2))
    time1.append(int(i[0], 2))
for i in dane2:
    temp2.append(int(i[1], 4))
    time2.append(int(i[0], 4))

for i in dane3:
    temp3.append(int(i[1], 8))
    time3.append(int(i[0], 8))

def dec2bin(number):
    number = abs(number)
    if number==0:
        return 0
    binary = ""
    while number>0:
        r = number % 2
        binary = str(r) + binary
        number = number//2
    return binary


min1,min2,min3 = min(temp1), min(temp2), min(temp3)
ans.write(f"ZADANIE 58.1\nStacja 1:-{dec2bin(min1)}\nStacja 2:-{dec2bin(min2)}\nStacja 3:-{dec2bin(min3)}\n\n")

#58.2
def isWrong(number):
    if (number-12)%24 != 0:
        return True
    return False

counter = 0
for i in range(len(time1)):
    if isWrong(time1[i]) and isWrong(time2[i]) and isWrong(time3[i]):
        counter += 1

ans.write(f"ZADANIE 58.2\n{counter}\n\n")

#58.3
rekord1, rekord2, rekord3 = [],[],[]
r1,r2,r3 = 0,0,0
indeksy = set()
for i in range(len(dane1)):
    if temp1[i] > r1:
        r1 = temp1[i]
        indeksy.add(i)
    if temp2[i] > r2:
        r2 = temp2[i]
        indeksy.add(i)
    if temp3[i] > r3:
        r3 = temp3[i]
        indeksy.add(i)
counter = 0
for i in indeksy:
    counter += 1
ans.write(f"ZADANIE 58.3\n{counter}\n\n")

#58.4
import math
skoki = []
for i in range(len(temp1)):
    for j in range(i+1,len(temp1)):
        r = (temp1[i] - temp1[j])**2
        skoki.append(math.ceil(r/abs(i-j)))
ans.write(f"ZADANIE 58.4\n{max(skoki)}\n\n")





ans.close()