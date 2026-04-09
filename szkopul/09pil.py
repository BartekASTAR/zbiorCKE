import math

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in numbers:
    if isPrime(i):
        print("TAK")
    else:
        print("NIE")
