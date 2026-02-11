from fontTools.misc.cython import returns

with open("liczby1.txt", "r") as f:
    file = [int(line) for line in f.readlines()]

print(file)

#62.1
ans = open("wyniki062.txt", "w")

ans.write(f"62.1\nMin: {min(file)}\nMax: {max(file)}\n\n")

#62.2
max_first = 0
max_counter = 0
for i in range(len(file)):
    counter = 1
    for j in range(i+1, len(file)):
        if file[j] < file[j-1]:
            if counter > max_counter:
                max_counter = counter
                max_first = file[i]
            break
        counter += 1
ans.write(f"62.2\nZaczyna sie: {max_first}\nDlugosc: {max_counter}\n\n")

#62.3
file8= file
with open("liczby2.txt", "r") as f:
    file10 = [int(line) for line in f.readlines()]

import math
def base2dec(base,number):
    decimal = 0
    for i in range(len(str(number))):
        d = number % 10
        decimal += d * math.pow(base, i)
        number //= 10
    return decimal

a,b = 0,0

for i in range(len(file8)):
    if base2dec(8, file8[i]) == file10[i]:
        a += 1
    elif base2dec(8, file8[i]) > file10[i]:
        b+= 1
ans.write(f"62.3\na) {a}\nb) {b}\n\n")

#62.4
counter10_6, counter8_6 =0,0
for i in file10:
    for j in str(i):
        if int(j) == 6:
            counter10_6 += 1

def dec2base(base, decimal):
    if decimal == 0:
        return "0"
    number = ""
    while decimal > 0:
        number = str(decimal % base) + number
        decimal //= base
    return number

for i in file10:
    for j in dec2base(8, int(i)):
        if int(j) == 6:
            counter8_6 += 1

ans.write(f"62.4\nW zapisie 10: {counter10_6}\nW zapisie 8: {counter8_6}")





