with open("krosno.txt", "r") as f:
    file = [int(line.strip()) for line in f.readlines()]

ans = open("wyniki2.txt", "w")
ans.write(f"2.1 NIE, NIE\n\n")

A = [8,3,3,2,9,8,6,8,8,10]

def czy_k_rosnaca(A,n,k):
    for i in range(n-k):
        if A[i] >= A[i+k]:
            return False
    return True

print(czy_k_rosnaca(A,10,5))

ans.write("2.4 ")
for i in range(len(file)):
    if czy_k_rosnaca(file, len(file), i):
        ans.write(f"{i} ")

