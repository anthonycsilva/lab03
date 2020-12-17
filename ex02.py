import math
def discriminante(a,b,c):
    "essa função calcula o discriminante dado as variáveis a,b,c"
    "int, int, int -> int"
    return math.pow(b, 2) - (4*a*c)



def calculaRaiz1(a,b,c):
    "essa função calcula a primeira raiz da equação  de segundo grau"
    "int, int, int -> float"

    return (-(b) + math.sqrt(discriminante(a,b,c)))/2*a



def calculaRaiz2(a,b,c):
    "essa função calcula a segunda raiz da equação  de segundo grau"
    "int, int, int -> float"
    return (-(b) - math.sqrt(discriminante(a,b,c)))/2*a

def verificaRaiz(a,b,c):
    if(discriminante(a,b,c)<0):
        return 0
    elif(discriminante(a,b,c) == 0):
        return  calculaRaiz1(a,b,c)
    elif(discriminante(a,b,c) > 0):
        return calculaRaiz1(a,b,c), calculaRaiz2(a,b,c)

print(verificaRaiz(1,-3, -10))


