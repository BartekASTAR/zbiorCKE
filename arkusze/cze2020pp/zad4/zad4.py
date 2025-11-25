with open("liczby.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]
    print(file)

    ans = open("wyniki4.txt", "w")
    #ZADANIE 4.1
    counter = 0
    for i in file:
      if int(i) % 2 != 0:
          counter += 1
    ans.write(f"ZADANIE 4.1\n{counter}\n\n")

    #ZADANIE 4.2
    def sum_digits(number):
        number = int(number)
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum

    ans.write("ZADANIE 4.2\n")
    for i in file:
        if sum_digits(i) == 11:
            ans.write(f"{i}\n")

    ans.write("\n")

    #ZDANIE 4.3
    import math
    def is_prime(number):
        number = int(number)
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                return False
        return True

    ans.write("ZADANIE 4.3\n")
    for i in file:
        if int(i)>=4000 and int(i) <= 5000 and is_prime(i):
            ans.write(f"{i}\n")
    ans.close()