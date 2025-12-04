counter = 0
def NWD(a,b):
    global counter
    counter = 0
    while b != 0:
        r = a % b
        counter += 1
        a = b
        b = r
    return a

poczatek = a1
for i in range(n):
    w = NWD(w, ai)