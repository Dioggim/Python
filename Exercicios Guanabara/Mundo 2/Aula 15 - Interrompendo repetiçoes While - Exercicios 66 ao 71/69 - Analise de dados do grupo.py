conti = contm = contf2 = idade = 0
sexo = c = ' '
print('---'*20)
print('Cadastro de Pessoas')
print('---'*20)
while True:
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        conti += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F':
        if idade < 20:
            contf2 += 1
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
    sexo = ' '
    c = ' '
print(f'Foram cadastradas {conti} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {contm} Homens.')
print(f'Foram cadastradas {contf2} Mulheres com menos de 20 anos.')