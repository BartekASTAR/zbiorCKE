import math

with open("t_trojki.txt", "r") as f:
    file = [list(map(int, line.strip().split())) for line in f.readlines()]
    ans = open("wyniki_trojki.txt", "w")

    def is_prime(n):
        if n == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

    #zad066.1
    ans.write("ZADANIE 66.1\n")
    for i in file:
        sum = 0
        for j in range(len(str(i[0]))):
            sum += int(str(i[0])[j])
        for j in range(len(str(i[1]))):
            sum += int(str(i[1])[j])
        if sum == i[2]:
            ans.write(f"{i[0]} {i[1]} {i[2]}\n")

    #zad 66.2
    ans.write("ZADANIE 65.2\n")
    for i in file:
        if is_prime(i[0]) and is_prime(i[1]) and i[2] == i[0] * i[1]:
            ans.write(f"{i[0]} {i[1]} {i[2]}\n")

    #zad 66.3
    ans.write("ZADANIE 65.3\n")
    for i in range(0, len(file)-1):
        maks_0 = max(file[i])
        maks_1 = max(file[i+1])
        przyp_0 = 0
        przyp_1 = 0
        for j in range(3):
            if file[i][j] == maks_0:
                continue
            przyp_0 += j**2
        for j in range(3):
            if file[i+1][j] == maks_1:
                continue
            przyp_1 += j**2
        if przyp_0 == maks_0**2 and przyp_1 == maks_1**2:
            ans.write(f"{i}\n{i+1}")


