print ('='*20)
print ('10 termos de uma PA')
print ('='*20)

termo = int(input('Digite o Termo (onde deve começar a Progressão Aritmética): '))
prog = int(input('Digite o valor da progressão: '))
c = 10
while c != 0:
    print(termo, '->', end=' ')
    termo += prog
    c -= 1


print('Fim')