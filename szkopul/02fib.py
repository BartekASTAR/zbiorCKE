n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    przedostatni, ostatni = 1,1
    for i in range(n-2):
        przedostatni, ostatni = ostatni, ostatni+przedostatni
    return ostatni

print(fib(n))