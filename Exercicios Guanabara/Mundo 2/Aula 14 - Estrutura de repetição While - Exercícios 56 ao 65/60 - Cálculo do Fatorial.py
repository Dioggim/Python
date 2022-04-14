num1 = int(input('Digite um número para calcular seu Fatorial: '))
num = num1
cont = num
while cont >= 1:
    cont = cont - 1
    if cont != 0:
        num = num * cont
print('O resultado de {}! em seu fatorial é {}.'.format(num1,num))
#-----------------------------------------------------------------------
#Versoes do professor Guanabara
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print ('O fatorial de {} é {}.'.format(n,f))
#-----------------------------------------------------------------------
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))
