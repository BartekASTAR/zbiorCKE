with open("pi_przyklad.txt", "r") as f:
    file = [line.strip() for line in f]

ans = open("wyniki3.txt","w")
#zad 3.1
counter = 0
for i in range(len(file)-1):
    frag = file[i:i+2]
    if int(str(frag[0] + str(frag[1]))) > 90:
        counter += 1
ans.write(f"ZADANIE 3.1\n{counter}\n\n")

#zadanie 3.2
ans.write(f"ZADANIE 3.2\n")
fragments = [0 for item in range(100)]
for i in range(len(file)-1):
    frag = file[i:i+2]
    fragments[int(str(frag[0] + str(frag[1])))] += 1
    fragments.index(min(fragments)),min(fragments))
    print(fragments.index(max(fragments)),(max(fragments)))