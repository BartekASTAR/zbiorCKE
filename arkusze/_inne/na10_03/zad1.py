#zad 1.3
def notacja(number):
    n = 0
    for i in str(number):
        n += int(i)
    number -= n
    return number // 9

print(notacja(2323454))
print(notacja(123456789))
print(notacja(222222222222))

#zad 1.4
def notacja2(number):
    n = 0
    for i in str(number):
        n += int(i)
    reszta = n % 9
    return number - reszta

print()
print(notacja2(34345))
print(notacja2(9800987))
print(notacja2(32289000))