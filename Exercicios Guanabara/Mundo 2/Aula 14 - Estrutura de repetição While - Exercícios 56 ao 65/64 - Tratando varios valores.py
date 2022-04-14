print('Brincadeira da Soma Infinita - para PARAR  digite 999\n\n\n')
n = int(input('Digite um numero sem vírgulas para acrescentar à soma: '))
cont = 0
soma= 0
while n != 999:
    soma += n
    cont +=1
    n = int(input('Digite outro número para acrescentar à soma: '))

print('Foram Digitados {} números e a soma entre eles é igual a {}.'.format(cont,soma))

