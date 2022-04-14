print('Vamos ver qual numero é maior...')
num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva um numero: '))

if num1>num2:
    maior = num1
    print('O maior numero é {}.'.format(num1))
elif num2>num1:
    maior = num2
    print('O maior numero é {}.'.format(num2))
elif num1 == num2:
    print('Eles são iguais!')
    maior = num1
