with open("ciagi.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

ans = open("wyniki063.txt", "w")

#63.1
ans.write(f"63.1\n")
for i in file:
    if len(i) % 2 != 0:
        continue
    first = i[:len(i)//2]
    second = i[len(i)//2:]
    if first == second:
        ans.write(f"{i}\n")

#63.2
counter = 0
for i in file:
    for j in range(len(i)-1):
        if i[j:j+2] == "11":
            break
    else:
        counter += 1
ans.write(f"\n63.2\n{counter}\n\n")

#63.3

import math
half_prime = []

def isPrime(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return  False
    return True

for k in file:
        first = None
        i = int(k,2)
        for j in range(2,int(math.sqrt(int(i))) + 1):
            if int(i) % j == 0:
                first = j
                break
        if first is not None:
            second = int(i) // first
            if isPrime(second) and isPrime(first):
                half_prime.append(i)
ans.write(f"63.3\nIle takich ciagow: {len(half_prime)}\nMin: {min(half_prime)}\nMax: {max(half_prime)}")
print(half_prime)
