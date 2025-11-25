with open("sygnaly.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

    print(file)

    ans = open("wyniki4.txt", "w")

    #ZADANIE 4.1
    ans.write("ZADANIE 4.1\n")
    message = ""
    for i in range(-1, len(file), 40):
        if i == -1:
            continue
        message += file[i][9]
    ans.write(f"{message}\n\n")

    #ZADANIE 4.2
    ans.write("ZADANIE 4.2\n")
    litery = []
    for i in file:
        temp = set()
        for j in range(len(i)):
            temp.add(i[j])
        litery.append(temp)
    ans.write(f"{file[litery.index(max(litery))]} {len(max(litery))}\n\n")

    #ZADANIE 4.3

    def less_than_10(word):
        for j in range(len(word)):
            for k in range(j,len(word)):
                if abs(ord(word[j]) - ord(word[k])) > 10:
                    return False
        return True

    ans.write("ZADANIE 4.3\n")
    for i in file:
        if less_than_10(i):
            ans.write(f"{i}\n")


    ans.close()