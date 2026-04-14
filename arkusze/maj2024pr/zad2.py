counter = 0
def cyfry(n):
    global counter
    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b*(a // 2)
        else:
            c = c + b
            counter += 1
        b = b * 10
    return c
counter = 0
print(cyfry(33658), counter)
counter = 0
print(cyfry(542102), counter)
counter = 0
print(cyfry(87654321012345678), counter)

