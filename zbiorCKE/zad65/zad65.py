import math
with open("dane_ulamki.txt", "r") as f:
    file = [list(map(int,line.strip().split())) for line in f.readlines()]
    print(file)

    ans = open("wyniki_ulamki.txt", "w")

    #zad 65.1
    min = 120000
    mianownik = 0
    ind = 0
    for i in file:
        if i[0]/i[1] < min:
            ind = file.index(i)
            min = i[0]/i[1]
            mianownik = i[1]
        elif i[0]/i[1] == min and i[1] < mianownik:
            ind = file.index(i)
            mianownik = i[1]

    ans.write(f"ZADANIE 65.1\n{file[ind][0]} {file[ind][1]}\n\n")

    #zad 65.2
    counter = 0
    for i in file:
        if math.gcd(i[0], i[1]) == 1:
            counter += 1
    ans.write(f"ZADANIE 65.2\n{counter}\n\n")

    #zad 65.3
    new_file = []
    sum = 0
    for i in file:
        gcd = math.gcd(i[0], i[1])
        if gcd == 1:
            new_file.append(i)
        else:
            temp = []
            temp.append(i[0]//gcd)
            temp.append(i[1]//gcd)
            new_file.append(temp)
    for i in new_file:
        sum += i[0]
    ans.write(f"ZADANIE 65.3\n{sum}\n\n")

    #zad 65.4
    b = 2**2 * 3**2 * 5**2 * 7**2 * 13
    sum = 0
    for i in file:
        sum += i[0]*b/i[1]
    ans.write(f"ZADANIE 65.5\n{int(sum)}\n\n")

    ans.close()




