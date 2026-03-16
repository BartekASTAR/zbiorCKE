s = 1023
A = [1,2,4,8,16,32,64,128, 256, 512]
print(A)
n=len(A)
B = ["" for i in range(0,s+1)]

def Tura(k):
    for i in range(s, A[k]-1, -1):
        if B[i - A[k]] == "x" and B[i] == "":
            B[i] = "x"
        #print(B)

B[0] = "x"
print(B)
for k in range(0, n):
    Tura(k)
    print(B)

#print(B.count("x"))


