import math

with open("liczby.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

print(file)

ans = open("wyniki60.txt","w")

#60.1
counter = 0
less1000 = []
for i in file:
    if int(i) < 1000:
        counter += 1
        less1000.append(i)

ans.write(f"60.1\nLiczb mniejszych niz 1000 jest: {counter}\n{less1000[-1]}\n{less1000[-2]}\n\n")

#60.2
ans.write("60.2\n")
divisors = []
for i in file:
    dividers = []
    n = int(i)
    for j in range(1, int(math.sqrt(n)) + 1):
        if n % j == 0:
            dividers.append(j)
            if j != n // j:
                dividers.append(n//j)

    print(f"{i} {dividers}")
    if len(dividers) == 18:
        ans.write(f"{i} {sorted(dividers)}\n")
    divisors.append(dividers)

#60.3

wzglist = []
for i in range(len(file)):
    wzgPier = True
    for j in range(i+1,len(file)):
        if math.gcd(int(file[i]), int(file[j])) != 1:
            wzgPier = False
            break
    if wzgPier:
        wzglist.append(file[i])
print(wzglist)
ans.write(f"\n\n60.3\n{max(wzglist)}")