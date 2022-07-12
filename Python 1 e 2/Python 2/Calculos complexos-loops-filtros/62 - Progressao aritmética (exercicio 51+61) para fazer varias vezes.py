#codigo para fazer até o usuário não querer mais.
print ('='*20)
print ('10 termos de uma PA')
print ('='*20)
c = 1
user ='s'

while user == 's':
    termo = int(input('Digite o Termo (onde deve começar a Progressão Aritmética): '))
    prog = int(input('Digite o valor da progressão: '))
    while c <= 10:
        print(termo, '->', end=' ')
        termo += prog
        c += 1

    print('Fim')

    user = str(input('Você deseja ver mais uma PA? [s/n]')).strip().lower()

    if user == 's':
        c = 1
    else:
        print('Você não digitou valor válido.')
print('Obrigado por usar o meu programa!')