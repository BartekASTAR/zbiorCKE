from Arkusze.maj2018pr.zad4.zad4 import less_than_10

with open("dane_przyklad.txt", "r") as f:
    file = f.readline()

    #ZADANIE 3.1
    #p=0
    #started = False
    #numbers = []
    #for n,i in enumerate(file):
    #    if i.isnumeric() and started==False:
    #        p = n
    #        started = True
    #    elif not i.isnumeric() and started==True:
    #        numbers.append(int(file[p:n]))
    #        started = False


    numbers = []
    number = ""
    for i in file:
        if i.isdigit():
            number += i
        elif number != "":
            numbers.append(int(number))
            number = ""

    ans = open("wyniki3.txt", "w")

    print(numbers)
    counter = 0
    for i in numbers:
        if str(i)[:2] == "50":
            counter += 1
    ans.write(f"ZADANIE 3.1\n{counter}\n\n")

    #ZADANIE3.2
    freq = [0 for _ in range(10)]
    for i in numbers:
        for j in str(i):
            freq[int(j)] += 1
    ans.write(f"ZADANIE 3.2\n{freq.index(max(freq))} {max(freq)}\n\n")

    #ZADANIE 3.3
    ans.write(f"ZADANIE 3.3\n")
    for i in numbers:
        if len(str(i)) == 9 and str(i)[0] == "5":
            ans.write(f"{i}\n")

    #ZADANIE 3.4
    list_sets = []
    for i in numbers:
        pass



