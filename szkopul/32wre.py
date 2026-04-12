#N = int(input())
#n = input()
#nominaly = list(map(int, input().split()))
#monety = 0
#i = 0
#while N>0:
#    if N - nominaly[i] >= 0:
#        monety +=1
#        N = N - nominaly[i]
#    else:
#        i+=1
#print(monety)

N = int(input())
n = input()
nominaly = list(map(int, input().split()))
monety = 0
i = 0
while N>0:
    if (N//nominaly[i])*nominaly[i] > 0:
        monety += N//nominaly[i]
        N = N - N//nominaly[i]*nominaly[i]
    else:
        i+=1
print(monety)