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


