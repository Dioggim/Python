from time import sleep
print('Teste dois números!')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('Escolha o que deseja fazer!\n ')
print('[1] Somar \ [2] Multiplicar\ [3] Qual é maior\ [4] Escolher outros números\ [5] Sair do programa\n')
opc = int(input('Digite a sua opção: '))
res = 0
while opc != 5:
    print('===*'*10)
    if opc == 1:
        res = n1 + n2
        print('A soma dos números é {}.'.format(res))
    elif opc == 2:
        res = n1 * n2
        print('A multiplicação dos números é {}.'.format(res))
    elif opc == 3:
        if n1>n2:
            res = n1
            print('O maior número é o {}.'.format(n1))
        elif n2> n1:
            res = n2
            print('O maior número é o {}.'.format(n2))
        else:
            print('Os numeros são iguais.')
    elif opc == 4:
        n1 = float(input('Digite novamento o primeiro número: '))
        n2 = float(input('Digite novamento o segundo número: '))
    else:
        print('Você nao digitou uma opção válida.')
    print('===*' * 10)
    print('E agora? O que deseja fazer?\n')
    print('[1] Somar \ [2] Multiplicar. \ [3] Qual é maior \ [4] Escolher outros números \ [5] Sair do programa\n')
    opc = int(input('Digite a sua opção: '))

print('Finalizando...')
sleep(1)
print('Obrigado por utilizar nosso programa! ')



