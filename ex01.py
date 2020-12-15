import math

def calculaAbs(x):
#essa função verifica o tipo de numero, e retorna o valor absoluto desse numero. Funciona somente com numeros inteiros ou float.
    x == int(x)
    if(x < 0):
        return x*(-1)
    else:
        return x