import random

x = (random.randint(1,1000))
print('Inteiros: {}'.format(x))

f = (random.random())
print('Float entre 0 e 1:  {:.4}'.format(f))

c  = 3j
k = random.randint(1,10) + ((random.randint(1,10) + 3j))

print('Numeros Complexos, onde J é imaginário: {}, {}'.format(c, k))