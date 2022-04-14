num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão
      [1] converter em BINÁRIO
      [2] converter em OCTAL
      [3] converter em HEXADECIMAL''')

opt = int(input('Sua opção: '))
if opt == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} convertido em HEXADECIMAL é igual a {:}'.format(num, hex(num)[2:]))

else:
    print('você nao digitou uma opção válida.')