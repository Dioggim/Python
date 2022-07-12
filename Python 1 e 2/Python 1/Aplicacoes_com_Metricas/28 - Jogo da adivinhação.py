import random
from time import sleep
print('-=--'*10)
print('Vou pensar em um numero de 0 a 5 , tente adivinhar...')
print('-=--')
x = int(input('Pense em um numero de 0 a 5:  '))
n = random.randint(0,5)

print('processando...')
sleep (3) #stop no programa pela quantidade de (segundos).

print('o nemero escolhido é {} e o numero que o pc escolheu é {}.'.format(x,n))

if x==n:
    print('Você acertou!! =)')
else:
    print('Você errou!! :(')

