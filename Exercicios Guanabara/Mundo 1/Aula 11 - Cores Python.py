#\033[x;y;zm inicio da coloração x y e z sao variaveis q representam as cores, olhar caderno indice de cores
print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[;4;33;44mOlá, Mundo!\033[m')
print('\033[4;34;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')

nome ='Diogo'

print("Olá! Muito prazer em te conhecer {} {} {}!!!".format('\033[7;40m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome , cores['limpa']))

