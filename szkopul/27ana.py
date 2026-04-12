n = int(input())
words = []
for _ in range(n):
    words.append(input().split())
for i in words:
    a,b = i
    if sorted(a) == sorted(b):
        print("TAK")
    else:
        print("NIE")