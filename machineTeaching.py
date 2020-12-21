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


print(classificacao(9,5,6,18,5,0))


