with open("punkty.txt", "r") as f:
    file = [line.strip().split() for line in f.readlines()]

    ans = open("wyniki4.txt", "w")

    #ZADANIE 4.1
    ans.write("ZADANIE 4.1\n")

    import math
    def is_prime(number):
        for i in range(2, int(math.sqrt(number))+1):
            if number%i == 0:
                return False
        return True

    counter = 0
    for i in file:
        if is_prime(int(i[0])) and is_prime(int(i[1])):
            counter += 1
    ans.write(f"{counter}\n\n")

    #ZADANIE 4.2
    counter = 0
    for i in file:
        set1, set2 = set(), set()
        for j in range(len(i[0])):
            set1.add(i[0][j])
        for j in range(len(i[1])):
            set2.add(i[1][j])
        if set1 == set2:
            counter += 1
    ans.write(f"ZADANIE 4.2\n{counter}\n\n")

    #ZADANIE 4.3
    max_distance = 0
    distance = 0
    point1, point2 = 0,0
    for i in range(len(file)):
        for j in range(i, len(file)):
            distance = math.sqrt(math.pow((int(file[i][0]) - int(file[j][0])), 2) + math.pow((int(file[i][1]) - int(file[j][1])),2))
            if distance > max_distance:
                max_distance = distance
                point1 = file[i]
                point2 = file[j]
    ans.write(f"ZADANIE 4.3\nPunnkt1: x:{point1[0]} y:{point1[1]}\nPunkt2: x:{point2[0]} y:{point2[1]}\nDystans: {int(max_distance)}\n\n")

    #ZADANIE 4.4
    ans.write("ZADANIE 4.4\n")

    wew, bok, zew =0, 0, 0
    for i in file:
        if int(i[0]) < 5000 and int(i[0]) > -5000 and int(i[1]) < 5000 and int(i[1]) > -5000:
            wew += 1
        elif int(i[0]) == 5000 or int(i[0]) == -5000 or int(i[1]) == 5000 or int(i[1]) == -5000:
            bok += 1
        else:
            zew += 1
    ans.write(f"wewnatrz kwadratu: {wew}\nna bokach kwadratu: {bok}\nna zewnatrz kwadratu{zew}")


    ans.close()