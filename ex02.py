import math
def discriminante(a,b,c):
    '''essa função calcula o discriminante dado as variáveis a,b,c'''
    '''float, float, float -> float'''
    return math.pow(b, 2) - (4*a*c)



def calculaRaiz1(a,b,c):
    '''essa função calcula a primeira raiz da equação  de segundo grau'''
    '''float, float, float -> float'''

    return (-(b) + math.sqrt(discriminante(a,b,c)))/2*a



def calculaRaiz2(a,b,c):
    '''essa função calcula a segunda raiz da equação  de segundo grau'''
    '''float, float, float -> float'''
    return (-(b) - math.sqrt(discriminante(a,b,c)))/2*a

def verificaRaiz(a,b,c):
    '''Essa função recebe as variáveis a,b,c e verifica se o discriminante é maior ou igual a 0 e retorna a raiz ou as raizes da equação'''
    '''float -> float'''
    if(discriminante(a,b,c)<0):
        return 0
    elif(discriminante(a,b,c) == 0):
        return  calculaRaiz1(a,b,c)
    elif(discriminante(a,b,c) > 0):
        return calculaRaiz1(a,b,c), calculaRaiz2(a,b,c)

print(verificaRaiz(1,-3, -10))


