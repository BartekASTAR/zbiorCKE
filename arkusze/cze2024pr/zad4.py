with open("odbiorcy_przyklad.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]
    file = list(map(int, file))

ans = open("wyniki4.txt", "w")

#4.2
ans.write(f"4.2\n")
computers = [i for i in range(1,len(file)+ 1)]
counter = 0
for i in file:
    if i not in computers:
        counter += 1
ans.write(f"{counter}\n\n")

#4.3
cycle = []
switch = True
cycle.append(computers)
cycle.append(file)

def print_cycle():
    for i in cycle:
        print(i)

print_cycle()

for i in range(2,20):
    pointer = 0
    row = [0 for _ in range(len(file))]
    for j in range(len(file)):
        for k in range(len(file)):
            if cycle[i-1][j] == cycle[i-2][k]:
                row[pointer] = cycle[i-1][k]
                break
        pointer += 1
    cycle.append(row)
    if switch:
        min_runda = len(cycle)-1
        min_pakiet = len(file)+ 1
        for l in range(len(row)):
            if row[l] == cycle[0][l]:
                switch = False
                if row[l] < min_pakiet:
                    min_pakiet = row[l]
ans.write(f"4.3\n{min_runda} {min_pakiet}")




print_cycle()

# 4.4
cycle = []

cycle.append(computers)
cycle.append(file)

print_cycle()

computers_dict = {}
for i in range(1,len(file)+ 1):
    computers_dict[i] = set()

for i, v in enumerate(file):
    computers_dict[i+1].add(v)



for i in range(2, 10):
    pointer = 0
    row = [0 for _ in range(len(file))]
    for j in range(len(file)):
        for k in range(len(file)):
            if cycle[i - 1][j] == cycle[i - 2][k]:
                row[pointer] = cycle[i - 1][k]
                break
        pointer += 1
    cycle.append(row)

