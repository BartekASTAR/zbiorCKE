with open("dane.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]
    print(file)

    ans = open("wyniki6.txt", "w")

    #ZADANIE 6.1
    male, female = 0,0
    for i in file:
        if int(i[-2]) % 2 == 0:
            female += 1
        else:
            male += 1
    ans.write(f"ZADANIE 6.1\nLiczba kobiet: {female}\nLiczba mezczyzn: {male}\n\n")

    #ZADANIE 6.2
    november = 0
    for i in file:
        if int(i[2:4]) == 11 or int(i[2:4]) == 31:
            november+= 1
    ans.write(f"ZADANIE 6.2\nLiczba osob urodzonych w listopadzie: {november}\n\n")

    #ZADANIE 6.3
    ans.write("ZADANIE 6.3\n")
    wagi = [1,3,7,9,1,3,7,9,1,3,1]
    for i in file:
        suma = 0
        for j in range(len(i)):
            suma += int(i[j])*wagi[j]
        if suma % 10 != 0:
            ans.write(f"{i}\n")

    ans.close()