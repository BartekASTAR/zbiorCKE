A = [[1], [1, 1]]

n = 10
for i in range(2, n + 1):
    B = [1]
    for j in range(1, i):
        B.append(A[i - 1][j - 1] + A[i - 1][j])
    B.append(1)
    A.append(B)

print(A)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(" ", end=" ")
    for j in range(len(A[i])):
        print(A[i][j], end=" ")
    print()