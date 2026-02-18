n = 19
def pow(n,p):
    result = 1
    for i in range(p):
        result *= n
    return result

counter = 0
def dec2bin(n):
    power = 0
    bin = 0
    while n > 0:
        bin += (n % 2) * pow(10,power)
        n //=2
        power += 1
    return bin

def J(n):
    power = 0
    while n > 0:
        digit = n % 2
        if digit == 1:
            print(power+1, end = " ")
        n //= 2
        power += 1

print(dec2bin(19))
J(19)
