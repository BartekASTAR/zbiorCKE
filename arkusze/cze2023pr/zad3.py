with open("anagram.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

print(file)

ans = open("wyniki3.txt", "w")

#3.1
zrow, przrow = 0,0

for i in file:
    jeden = i.count("1")
    zero = i.count("0")
    if jeden == zero:
        zrow += 1
    elif abs(jeden - zero) == 1:
        przrow  += 1

ans.write(f"3.1\n{zrow}\n{przrow}\n\n")

import math

#3.2
max_komb = 0
anagramy = []
for i in file:
    if len(i) != 8:
        continue
    jeden = i.count("1")
    zero = i.count("0")
    jeden -= 1
    kombinacje = math.comb(7,jeden)
    anagramy.append([i,kombinacje])
    if kombinacje > max_komb:
        max_komb = kombinacje

ans.write("3.2\n")
for i in anagramy:
    if i[1] == max_komb:
        ans.write(f"{i[0]}\n")

#3.3
max_abs = 0

def dec2bin(number):
    bin = ""
    while number > 0:
        digit = number % 2
        bin =  str(digit) + bin
        number //= 2
    return bin



for i in range(len(file)-1):
    t = abs(int(file[i], 2) - int(file[i+1],2))
    if t > max_abs:
        max_abs = t
ans.write(f"\n\n3.3\n{dec2bin(max_abs)}\n\n")

#3.4
dec_file = []
no_zero = 0
max_sum_digit = 0
value = 0
for i in file:
    dec_file.append(int(i,2))
for i in dec_file:
    if "0" not in str(i):
        no_zero += 1
    digits = set(str(i))
    sum_digit = sum(map(int, digits))
    if sum_digit > max_sum_digit:
        max_sum_digit = sum_digit
        value = i
ans.write(f"3.4\n{no_zero}\n{value}")
