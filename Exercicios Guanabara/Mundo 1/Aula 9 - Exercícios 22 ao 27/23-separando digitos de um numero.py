n = int(input('Digite um numero inteiro entre 0 e 9999'))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print ('O numero inteiro é {}'.format(n))
print ('Unidade é {}'.format(u))
print ('Dezena {}'.format(d))
print ('Centena {}'.format(c))
print ('Milhar {}'.format(m))