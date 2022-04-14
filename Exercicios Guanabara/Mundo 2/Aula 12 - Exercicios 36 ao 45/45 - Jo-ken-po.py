import random
from typing import List
import emoji

import emoji
import time


print ('Vamos jogar Jokenpô...')


print('''Voce tem 3 opçoes:
[0] Pedra
[1] Papel
[2] tesoura ''')

p1 = int(input(' Escolha a sua jogada: '))

lista = ('Pedra','Papel','Tesoura')

pc = random.randint (0,2)

if 0 <= p1 <= 2:

    #codigo para fazer a imagem do JO - KEN -PO com 1 segundo de espera por comando
    print('\033[1;41mJO\033[m')
    time.sleep(1)
    print('\033[1;43mKEN\033[m')
    time.sleep(1)
    print ('\033[1;46mPô!!!\033[m')

    print ('O computador escolheu {}.'.format(lista[pc]))
    print ('você escolheu {}.'.format(lista[p1]))
    if pc == 0:
        if p1 == 0:
            print('Foi um empate!')
        elif p1 == 1:
            print('Parabens você ganhou!')
        elif p1 == 2:
            print('Que pena, você perdeu!')

    elif pc == 1:
        if p1 == 0:
            print('Que pena, você perdeu!')
        elif p1 == 1:
            print('Foi um empate!')
        elif p1 == 2:
            print('Parabens você ganhou!')
    elif pc == 2:
        if p1 == 0:
            print('Parabens você ganhou!')
        elif p1 == 1:
            print('Que pena, você perdeu!')
        elif p1 == 2:
            print('Foi um empate!')
    else:
        p1 = 0
        print ('Você não escolheu uma opção válida')
else:
    print('Você digitou um valor inválido.')