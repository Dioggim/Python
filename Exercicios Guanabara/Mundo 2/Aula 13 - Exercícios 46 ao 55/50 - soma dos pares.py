print ('='*20)
print('Bem vindo ao analisador de numeros!')
print('Digite 6 numeros inteiros e lhe mostraremos a soma dos pares entre eles!')
print ('='*20)
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))

    if num % 2 == 0:
        soma += num
        cont += 1

print('Foram considerados {} numeros pares!'.format(cont))
print('A soma dos pares é {} !'.format(soma))
print('Acabou')