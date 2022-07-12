print ('='*20)
print ('10 termos de uma PA')
print ('='*20)

termo = int(input('Digite o Termo (onde deve começar a Progressão Aritmética): '))
prog = int(input('Digite o valor da progressão: '))

for c in range(termo,termo + prog * 10,prog):

    print(termo,'->',end=' ')
    termo += prog

print('acabou')

