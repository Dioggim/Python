km = float(input('Escreva a quantidade de Km rodados: '))
d = float(input('Quantidade de dias alugado: '))

print (' o carro rodou {} km em {} dias.'.format(km,d))

pkm= km*0.15
pd= d*60

print(' O preço do alugue por dia ficou em R$ {} e a taxa de kilometragem R$ {}.'.format(pd,pkm))

total= pkm+pd

print('Totalizando R$ {}'.format(total))