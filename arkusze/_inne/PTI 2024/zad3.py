counter = 0
def kop(A,n,m,i,j):
    global counter
    if i == 3 and j == 3:
        counter += 1
    if i >= n or j >= m:
        return 0
    k1 = kop(A,n,m, i+1,j)
    k2 = kop(A,n,m,i,j+1)
    if k1 > k2:
        return A[i][j] + k1
    else:
        return A[i][j] + k2


def KopIter(A,n,m):
    B = [[0]*m for i in range(n)]
    for x in range(n):
        for y in range(m):
            if x == 0 and y == 0:
                B[x][y] = A[x][y]
            elif x == 0:
                B[x][y] = A[x][y] + B[x][y-1]
            elif y == 0:
                B[x][y] = A[x][y] + B[x-1][y]
            else:
                if B[x][y-1] > B[x-1][y]:
                    B[x][y] = A[x][y] + B[x][y - 1]
                else:
                    B[x][y] = A[x][y] + B[x - 1][y]
    return B[n-1][m-1]
            #B[x][y] = A[x][y] + góra LUB lewo (co większe)


A = [[4,2,1,10,5],
     [0,4,22,2,8],
     [40,1,1,1,1]]

B = [[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0]]

n,m = 5,5

i, j = 1,1

#print(kop(A, n,m,i-1,j-1)), print(counter)
print(KopIter(A,3,5))