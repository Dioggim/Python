num =int(input('Digite um numero inteiro: '))
contp = 0
for c in range(1,num+1):
    if num % c == 0:
        contp += 1
        print('\033[33m{}\033[m'.format(c),end=' ')
    else:
        print('\033[31m{}\033[m'.format(c),end=' ')
if contp == 2:
    print('\nO número {} é primo.'.format(num))

else:
    print('\nO número {} não é primo.'.format(num))

print('O numero {} foi divisível {} vezes.'.format(num,contp))

