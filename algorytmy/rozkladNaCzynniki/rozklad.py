import math

n = int(input())

divisors = []
for j in range(1, int(math.sqrt(n)) + 1):
     if n % j == 0:
         divisors.append(j)
         if j != n // j:
             divisors.append(n//j)

print(f"{n} : {sorted(divisors)}")