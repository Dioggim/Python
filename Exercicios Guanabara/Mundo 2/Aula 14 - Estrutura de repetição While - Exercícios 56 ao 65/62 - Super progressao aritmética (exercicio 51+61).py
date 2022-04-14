print('=' * 20)
print('10 termos de uma PA')
print('=' * 20)
c = 1
termo = int(input('Digite o Termo (onde deve começar a Progressão Aritmética): '))
prog = int(input('Digite o valor da progressão: '))
user = 10
total = 0
while user > 0:
    while c <= user:
        print(termo, '->', end=' ')
        termo += prog
        c += 1
        total += 1
    print('Fim')

    user = int(input('Digite quantos termos voce deseja ver a mais: '))
    if user > 0:
        c = 1
print('Foram mostrados {} termos da PA.'.format(total))
print('Obrigado por usar o meu programa!')