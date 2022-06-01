import math

liczba= []
liczba_figur= int(input())
for i in range(liczba_figur):
    liczba.append(input().split(" "))


def pole_kola(r):
    return math.pi*r*r

def pole_prostokata(a,b):
    return a*b

def pole_trojkata(x,y,z):
    p= (x+y+z)/2
    return math.sqrt(p*((p-x)*(p-y)*(p-z)))

pole= 0
for dane in liczba:
    if len(dane)== 1:
        kolo= pole_kola(float(dane[0]))
        pole += kolo
    elif len(dane)== 2:
        prostokat= pole_prostokata(float(dane[0]), float(dane[1]))
        pole += prostokat
    elif len(dane)== 3:
        trojkat= pole_trojkata(float(dane[0]), float(dane[1]), float(dane[2]))
        pole += trojkat
    elif len(dane)> 3:
        print("Błąd: można podać maksymalnie 3 liczby")
    
print(round(pole, 2))
 
