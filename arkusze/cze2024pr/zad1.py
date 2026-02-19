def power(n,k):
    if k == 0:
        return 1
    number = 1
    for i in range(k):
        number *= n
    return number

def dec2bin(n):
    binary = 0
    pow = 0
    while n>0:
        binary += n%2 * power(10, pow)
        n //= 2
        pow += 1
    return binary

def length(n):
    counter = 0
    while n > 0:
        n //= 10
        counter += 1
    return counter

n = 72
w,k = 4,3

tablica = w * k
ktora_od_poczatku = tablica % length(dec2bin(n))
binarka = dec2bin(n)
print(binarka)
print(ktora_od_poczatku)
if ktora_od_poczatku == 0:
    x = binarka % 10
else:
    for i in range(length(dec2bin(n)) - ktora_od_poczatku + 1):
        print(binarka)
        x = binarka % 10
        binarka //= 10
print(x)






