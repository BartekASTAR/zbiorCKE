def bin_search(tab, szuk):
    l = 1
    r = len(tab)
    while l <= r:
        print(f"[{l}, {r}]")
        m = int((l+r)/2)
        if tab[m] == szuk:
            print(m+1)
            return m+1
        elif tab[m] < szuk:
            l = m+1
        elif tab[m] > szuk:
            r = m-1
        elif l > r:
            return -1


n = int(input())
tabs = []
szukamy = []
for _ in range(n):
    a = input()
    tabs.append(list(map(int, input().split())))
    szukamy.append(int(input()))

for i in range(len(tabs)):
    bin_search(tabs[i], szukamy[i])
    print()