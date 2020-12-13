import random

x = (random.randint(1,1000))
print('Inteiros: {}'.format(x))

f = (random.random())
print('Float entre 0 e 1:  {:.4}'.format(f))

c  = 3j
k = random.randint(1,10) + ((random.randint(1,10) + 3j))

print('Numeros Complexos, onde J é imaginário: {}, {}'.format(c, k))

s = 'Isso é uma string, String é tudo escrito dentro das aspas simples ou duplas!'
exemplo1 = 'Como isso é uma string o python vê isso como: 3 + 5'
print(s)
print(exemplo1)

conta = '3+5'

print('A  conta só retorna o texto escrito!: {}'.format(conta))
