import math
def verifica1(x):
    '''Essa função retorna um valor para um dado x, seguindo o gráfico do exercício 5 lab03'''
    '''float -> float'''
    
    if (x>=0 and x<2):
        return x
    elif (x >= 2 and x <= 3.5):
        return 2
    elif (x>3.5 and x<=5):
        return 3
    else:
        return math.pow(x,2) -10*x + 20

