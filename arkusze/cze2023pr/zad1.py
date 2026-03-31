counter = 0
def iloczyn(x,y):
    global counter
    if y == 1:
        return x
    else:
        k = y // 2
        z = iloczyn(x,k)
        if y % 2 == 0:
            counter += 1
            return  z + z
        else:
            counter += 2
            return x + z + z

counter = 0
print(iloczyn(9,11), counter)
counter = 0
print(iloczyn(8,32), counter)
counter = 0
print(iloczyn(2,47), counter)
counter = 0
print(iloczyn(112,112), counter)


def iter_iloczyn(x,y):
    z = 0
    while y>0:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z

print(iter_iloczyn(0,112))