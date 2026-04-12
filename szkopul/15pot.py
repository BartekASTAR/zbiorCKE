import math

n = int(input())
triangles = []
for _ in range(n):
    triangles.append(list(map(int, input().split())))

for i in range(n):
    a,b,c = triangles[i]
    counter = 0
    if a+b>c:
        counter+=1
        print(f"{a} + {b} > {c}? TAK")
    else:
        print(f"{a} + {b} > {c}? NIE")
    if a+c>b:
        counter += 1
        print(f"{a} + {c} > {b}? TAK")
    else:
        print(f"{a} + {c} > {b}? NIE")
    if b+c>a:
        counter += 1
        print(f"{b} + {c} > {a}? TAK")
    else:
        print(f"{b} + {c} > {a}? NIE")
    if counter == 3:
        print(f"Trojkat: TAK")
        s = (a+b+c)/2
        Pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"s = {"{:.2f}".format(s)}")
        print(f"Pole = {"{:.2f}".format(Pole)}\n")
    else:
        print(f"Trojkat: NIE\n")