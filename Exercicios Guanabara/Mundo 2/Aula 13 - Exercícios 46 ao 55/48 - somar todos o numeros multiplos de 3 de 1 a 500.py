soma = 0
cont = 0
for c in range(3,501,1):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c)
            cont = cont + 1  #as duas operações sao iguais essa e a de baixo
            soma += c         # Essas duas




print('A soma é {}.'.format(soma))
print('Foram somados {}.'.format(cont))
print('acabou')