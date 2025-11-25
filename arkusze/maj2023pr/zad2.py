def dec2bin(number):
    binary = 0
    i = 1
    while number > 0:
        binary += number%2 * i
        number = number//2
        i = i *10
    return binary
def howManyBlocks(number):
    #number = dec2bin(number)
    blocks = 1
    last = number%10
    number = number//10
    while number > 0:
        current = number % 10
        if last != current:
            blocks +=1
        last = current
        number = number//10
    return blocks
    #print(blocks)

with open("bin.txt", "r") as f:
    file = [int(line.strip()) for line in f]

ans = open("wyniki2.txt", "w")

#zad 2.2
counter = 0
for i in file:
    if howManyBlocks(i) <= 2:
        counter += 1
ans.write(f"ZADANIE 2.2\n{counter}\n\n")

#zad 2.3
ans.write(f"ZADANIE 2.3\n{max(file)}\n\n")

#zad 2.5
ans.write("ZADANIE 2.5\n")
for i in file:
    odp = int(str(i),2) ^ int(str(i),2) // 2
    ans.write(f"{dec2bin(odp)}\n")

