import math

def calculaAbs(x):
    '''essa função verfica o numero inteiro ou float, e retorna seu valor absoluto!'''
    '''float -> float'''
    if(x<0):
        return  x*(-1)
    else:
        return x


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
#Na no arquivo de entrega, não conegui fazer funcionar com o import da aula anterior. decidi colocar o código aqui para que funcionasse.
    if(discriminante(a,b,c)<0):
        return 0
    elif(discriminante(a,b,c) == 0):
        return  calculaRaiz1(a,b,c)
    elif(discriminante(a,b,c) > 0):
        return calculaRaiz1(a,b,c), calculaRaiz2(a,b,c)

def  mensagem(m,n):
    "essa função repete a  mensagem 'm' um numero n de vezes, onde n é um numero inteiro"
    return n*m

def data(d,m,a):
    '''Essa função retorna em os numeros inseridos como dia/mes/ano'''
    '''int -> int'''
    if (d < 10 and m < 10):
        return str(0)+str(d)+'/'+str(0)+str(m)+'/'+str(a)
    elif(m < 10):
        return str(d)+'/'+str(0)+str(m)+'/'+str(a)
    elif(d < 10):
        return str(0) + str(d) + '/' + str(m) + '/' + str(a)
    else:
        return str(d)+'/'+str(m)+'/'+str(a)


def valorY(x):
    '''Essa função retorna um valor para um dado x, seguindo o gráfico do exercício 5 lab03'''
    '''float -> float'''

    if (x >= 0 and x < 2):
        return x
    elif (x >= 2 and x <= 3.5):
        return 2
    elif (x > 3.5 and x <= 5):
        return 3
    else:
        return math.pow(x, 2) - 10 * x + 20


def descontoImposto(s):
    '''Essa função recebe o salario bruto e retorna o desconto específico de cada salario'''
    '''float -> float'''
    if(s <=2000):
        return ((6/100) * s)
    elif(s>2000 and s<=3000):
        return (8/100)*s
    elif(s>3000):
        return (10/100)*s

def impostoRenda(s):
    '''Essa função recebe o salário bruto e retorna o imposto de renda específico do valor do salário bruto'''
    '''float -> float'''
    if(s<=2500):
        return (11/100)*s
    elif(s>2500 and s<=5000):
        return (15/100)*s
    elif(s>5000):
        return (22/100)*s

def salarioLiquido(s):
    '''Essa função recebe o salário bruto e retorna o salario líquido'''
    '''float -> float'''
    return (s-(descontoImposto(s)+impostoRenda(s)))


