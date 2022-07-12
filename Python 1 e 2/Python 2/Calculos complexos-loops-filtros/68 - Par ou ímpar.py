from random import randint
print('Vamos jogar Par ou ímpar')
cont = 0
while True:
    escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    if escolha in 'PI':
        p1 = int(input('coloque um número: '))
        pc = randint(1,10)
        soma = p1 + pc
        print(f'você escolheu {p1} e o PC colocou {pc}.', end='')
        if escolha == 'P':
            if soma % 2 == 0:
                print('Parabéns, você ganhou!')
                cont += 1
            else:
                print('Que pena, você perdeu!')
                break
        elif escolha == 'I':
            if soma % 2 == 0:
                print('Que pena, você perdeu!')
                break
            else:
                print('Parabéns, você ganhou!')
                cont += 1
print(f'O resultado foi {soma}, você venceu {cont} vezes!', end='')