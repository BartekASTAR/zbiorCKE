p = 4
n = 4
A = [3,1,2,2]
B = [0,0,2,1]
A = A[::-1]
B = B[::-1]
C = [0 for i in range(n+1)]

for i in range(n):
    sum = A[i] + B[i] + C[i]
    C[i] = sum % p
    C[i+1] = sum // p

print(C[::-1])