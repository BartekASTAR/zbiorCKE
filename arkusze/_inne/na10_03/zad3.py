#zad 3.1
def czyWspolliniowe(Xa, Ya, Xb, Yb, Xc, Yc):
    return (Yc - Ya)*(Xb-Xa) - (Yb - Ya)*(Xc - Xa) == 0

#print(czyWspolliniowe(0,1.5,-3,7.5,4,-6.5))
#print(czyWspolliniowe(-4.5,0.75,2,4,3.5,5))
#print(czyWspolliniowe(3.5,-7.25,-1.5,-0.25,1,-3.5))

#zad 3.3
with open("dane.txt", "r") as f:
    file = [list(map(float,line.strip().split())) for line in f.readlines()]
    print(file)

def prosta(Xa, Ya, Xb, Yb):
    return [(Ya-Yb), (Xb-Xa), ((Ya*Xb) - (Xa*Yb))] # Wpsolczynniki A,B,C prostej

def punktPrzecieca(p1, p2):
    W = p1[0]*p2[1] - p2[0]*p1[1]
    Wx = p1[2]*p2[1] - p2[2]*p1[1]
    Wy = p1[0]*p2[2] - p2[0]*p1[2]
    if W != 0:
        x = Wx / W
        y = Wy / W
        return [x,y]
    elif Wx == 0 and Wy == 0:
        return "TAK"
    else:
        return "NIE"

for i in file:
    AB = prosta(i[0], i[1], i[2], i[3])
    CD = prosta(i[4], i[5], i[6], i[7])
    if punktPrzecieca(AB,CD) != "NIE" and punktPrzecieca(AB,CD) != "TAK":
        x, y = punktPrzecieca(AB, CD)
        xAB, yAB, xCD, yCD = [i[0], i[2]],[i[1], i[3]],[i[4],i[6]],[i[5], i[7]]
        if ((min(xAB) <= x <= max(xAB)) and
            (min(xCD) <= x <= max(xCD)) and
            (min(yAB) <= y <= max(yAB)) and
            (min(yCD) <= y <= max(yCD))):
            print("TAK")
        else:
            print('NIE')
    elif punktPrzecieca(AB,CD) == "TAK" and (min(xAB) < min(xCD) < max(xAB) < max(xCD) or min(xCD) < min(xAB) < max(xCD) < max(xAB) or min(xCD) < min(xAB) < max(xAB) < max(xCD) or min(xAB) < min(xCD) < max(xCD) < max(xAB)):
        print("TAK")
    else:
        print('NIE')