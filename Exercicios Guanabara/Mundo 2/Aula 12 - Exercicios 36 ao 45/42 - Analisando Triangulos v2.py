print('Teste do triangulo! Digite os lados do triangulo!')
r1 = int(input('Digite lado 1: '))
r2 = int(input('Digite lado 2: '))
r3 = int(input('Digite lado 2: '))

if r1 <r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Estes comprimentos formam triangulo!')

    if r1 == r2 and r1==r3:
        print('O triangulo é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('O triangulo é ESCALENO')
    else:
        print('O triangulo é ISÓCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIANGULO!')
