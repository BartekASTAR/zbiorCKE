counter = 0
def F(x,p):
    global counter
    counter += 1
    if x == 0:
        return 0
    c = x % p
    if c % 2 == 1:
        return F(x//p,p) + c
    else:
        return F(x//p,p) - c

print(F(97,4), counter)