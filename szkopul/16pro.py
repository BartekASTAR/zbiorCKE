n = int(input())
triangles = []
for _ in range(n):
    triangles.append(list(map(int, input().split())))
for i in triangles:
    x,y,z = sorted(i)
    if x*x + y*y == z*z:
        print("TAK")
    else:
        print("NIE")

