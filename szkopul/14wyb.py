def bin_search(tab, szuk):
    l = 0
    r = len(tab)-1
    while l <= r:
        print(f"[{l+1}, {r+1}]")
        m = (l+r)//2
        if tab[m] == szuk:
            print(m+1)
            return m+1
        if tab[m] < szuk:
            l = m+1
        if tab[m] > szuk:
            r = m-1
    if l > r:
        print(-1)
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