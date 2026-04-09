n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

def sum_len(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n//10
    return sum
for n in numbers:
    cyfr = sum_len(n)
    if cyfr % 2== 0:
        print(f"{cyfr} PARZYSTA")
    else:
        print(f"{cyfr} NIEPARZYSTA")