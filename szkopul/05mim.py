n = int(input())
l_tab = []
tab_liczb = []
for i in range(n):
    l_tab.append(int(input()))
    tab_liczb.append(list(map(int, input().split())))
for i in range(n):
    if l_tab[i] % 2 == 0:
        if tab_liczb[i][0] > tab_liczb[i][1]:
            min, max = tab_liczb[i][1], tab_liczb[i][0]
        else:
            min, max = tab_liczb[i][0], tab_liczb[i][1]
        for j in range(2, l_tab[i]-1):
            if tab_liczb[i][j] > tab_liczb[i][j+1]:
                mniej, wiecej = tab_liczb[i][j+1], tab_liczb[i][j]
            else:
                mniej, wiecej = tab_liczb[i][j], tab_liczb[i][j+1]
            if min > mniej:
                min = mniej
            if max < wiecej:
                max = wiecej
    else:
        min, max = tab_liczb[i][0], tab_liczb[i][0]
        for j in range(1, l_tab[i]-1):
            if tab_liczb[i][j] > tab_liczb[i][j+1]:
                mniej, wiecej = tab_liczb[i][j+1], tab_liczb[i][j]
            else:
                mniej, wiecej = tab_liczb[i][j], tab_liczb[i][j+1]
            if min > mniej:
                min = mniej
            if max < wiecej:
                max = wiecej
    print(f"Min: {min} Max: {max}")