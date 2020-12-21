import math
def classificacao(cv,ce,cs,fv,fe,fs):
    c = (cv*3)+ce
    f = (fv*3)+fe
    print(c,f)

    if (c == f):
        if (cs == fs):
            return 'Empate'
        elif (cs > fs):
            return 'Cormengo'
        elif (fs > cs):
            return 'Flaminthians'

    if(c>f):
        return 'Cormengo'
    else:
        return 'Flaminthians'





def avioes(c, p_compr, p_compet):
    if((p_compr//p_compet)>=c):
        return 'Suficiente'
    else:
        return 'Insuficiente'

