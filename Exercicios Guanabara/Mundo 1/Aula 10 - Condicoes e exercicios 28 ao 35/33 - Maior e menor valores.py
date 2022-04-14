#dois jeitos diferentes de fazer
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
n3 = int(input('Digite um numero inteiro: '))
print('Os números são {}, {} e {}'.format(n1,n2,n3))

if n1>n2 and n1>n3:
    print ('O maior entre eles é o {}'.format(n1))
if n2>n1 and n2>n3:
    print ('O maior entre eles é o {}'.format(n2))
else:
    print ('O maior entre eles é o {}'.format(n3))

menor = n1

if n2<n1 and n2<n3:
    menor =n2
if n3<n1 and n3<n2:
    menor = n3
print ('O menor entre eles é o {}'.format(menor))



