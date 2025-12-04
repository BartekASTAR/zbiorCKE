def Fibonacccie(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacccie(n-1) + Fibonacccie(n-2)

fib_tab = [0,1,1]
for i in range(3,41):
    fib_tab.append(Fibonacccie(i))

def dec_2_bin(n):
    number = [0 for _ in range(27)]
    counter = 1
    while n > 0:
        number[-counter] = n%2
        n = n//2
        counter += 1
    return number

file = open("fib_tab.txt", "w")
fib_tab_bin = []
for i in fib_tab:
    file.write(f'{str(dec_2_bin(i))}\n')
    fib_tab_bin.append("".join(map(str,dec_2_bin(i))))

ans = open("wyniki67.txt", "w")
#ZADANIE 67.1
ans.write(f"ZADANIE 67.1\n{fib_tab[10]}\n{fib_tab[20]}\n{fib_tab[30]}\n{fib_tab[40]}\n\n")

#ZADANIE 67.2
import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

ans.write("ZADANIE 67.2\n")
for i in range(3,41):
    if isPrime(fib_tab[i]):
        ans.write(f"{fib_tab[i]}\n")

#67.4
ans.write(f"\n\nZADANIR 67.4\n")
fib_tab_bin.pop(0)
for i in fib_tab_bin:
    if str(i).count("1") == 6:
        ans.write(f"{i}\n")


