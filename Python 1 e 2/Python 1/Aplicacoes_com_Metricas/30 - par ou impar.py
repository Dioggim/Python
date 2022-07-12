x = int(input('Digite um numero inteiro: '))

n = x%2

print(n)

if n >= 1:
    print ('O numero {}, é Impar'.format(x))
else:
    print('O numero {}, é Par'.format(x))
