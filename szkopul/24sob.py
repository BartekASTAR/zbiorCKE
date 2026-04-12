n = int(input())
lista = list(map(int, input().split()))

def bubble_sort(n, lista):
    counter = 0
    for i in range(n-1):
        for j in range(0,n-1-i):
            if lista[j] > lista[j+1]:
                counter += 1
                lista[j], lista[j + 1] = lista[j+1], lista[j]
    return lista, counter
sorted = bubble_sort(n,lista)
for i in sorted[0]:
    print(i, end=" ")
print()
print(sorted[1])