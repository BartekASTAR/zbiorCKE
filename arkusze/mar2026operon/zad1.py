nominaly = [500,200,100,50,20,10,5,2,1]

def reszta(kwota, k=0):
    if kwota <= 0:
        return 0
    x = kwota // nominaly[k]
    print(nominaly[k], x)
    kwota = kwota - (x*nominaly[k])
    return x + reszta(kwota, k+1)


def reszta2(kwota):
    x,k = 0,0
    while kwota > 0:
        if kwota - nominaly[k] >= 0:
            kwota = kwota - nominaly[k]
            x += 1
        else:
            k+=1
    return x


print(reszta2(804))