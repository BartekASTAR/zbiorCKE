def nwd(a,b):
    if b == 0:
        return a
    return nwd(b, a % b)

def nwd_print(a,b, iloczyn):
    if b == 0:
        print(f"NWD: {a}\nNWM: {int(iloczyn/a)}\n")
        return a
    print(f"NWD({a}, {b}) = NWD({b}, {a % b})")
    return nwd_print(b, a % b, iloczyn)

n = int(input())
a_b = []
for _ in range(n):
    a_b.append(list(map(int, input().split())))
for i in a_b:
    a,b = i
    nwd_print(a,b, a*b)