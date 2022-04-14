print('Vamos ver a média!\n\n')
n = 0
c = 's'
cont = media = soma = maior = menor = seg = 0
while c == 's':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    media = soma/cont
    seg = 0
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Digite "s" para continuar ou "n" para parar.')).strip().lower()
    if c == 's' or c == 'n':
        seg = 1
    while seg != 1:
        if c == 's' or c == 'n':
            seg = 1
        else:
            c = str(input('Valor invalido. Digite "s" para continuar ou "n" para parar.')).strip().lower()
print('=*=-'*20)
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
print('A média dos valores digitados foi {:.2f}'.format(media))
print('Foram digitados {} valores'.format(cont))
print('=*=-'*20)

print('\033[1;7mFim\033[m')

