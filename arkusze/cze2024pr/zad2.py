counter = 0
def f(x):
    global counter
    counter += 1
    if x == 0:
        return 0
    else:
        return 2 + f(x // 2)

print(f(16), counter)

for i in range(0, 10000):
    if f(i) == 18:
        print(i)
        break


for i in range(10000, 0, -1):
    if f(i) == 18:
        print(i)
        break