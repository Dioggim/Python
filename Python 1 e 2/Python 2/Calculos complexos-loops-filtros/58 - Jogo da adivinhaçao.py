'''import random
print('Sou seu computador, acabei de pensar um número entre 1 e 10!\nTente adivinhar o número que o computador pensou!')
pc = random.randint(1,10)
user = int(input('Digite um numero entre 1 e 10: '))
cont = 1
while pc!= user:
    ver = user - pc
    if ver > 0:
        user = int(input('Menos... Tente novamente: ' ))
        cont += 1
    elif ver < 0:
        user = int(input('Mais... Tente novamente: '))
        cont += 1

print('Você acertou , foram necessarias {} tentativas e o número correto era {}.'.format(cont,pc))'''

#-----------------------------------------------------------------------------------------------------
#versao do professo Guanabara
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entreo 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

