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

