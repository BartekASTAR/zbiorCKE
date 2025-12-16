with open("NAPIS.TXT", "r") as f:
    file = [line.strip() for line in f.readlines()]
    print(file)

    ans = open("wyniki5.txt", "w")

    import math
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True

    #5.1
    ans.write("5.1\n")
    counter = 0
    for i in file:
        suma = 0
        for letter in i:
            suma += ord(letter)
        if is_prime(int(suma)):
            counter += 1
    ans.write(f"{counter}\n")

    #5.2
    ans.write("\n5.2\n")
    for i in file:
        max = ord(i[0]) - 1
        for j in i:
            if ord(j) > max:
                max = ord(j)
            else:
                break
        else:
            ans.write(f"{i}\n")

    #5.3
    ans.write("\n5.3\n")
    wyrazy = set()
    for i in file:
        if i in wyrazy:
            ans.write(f"{i}\n")
        else:
            wyrazy.add(i)




    ans.close()