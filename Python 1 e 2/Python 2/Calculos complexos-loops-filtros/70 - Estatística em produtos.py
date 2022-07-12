print('{:-^40}'.format('\033[1;7m Programa de estatísticas de compras\033[m'))
contp1000 = total = prodb = cont = 0
maisbarato = c = ' '

while True:
    prod = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: '))
    total += preco
    cont += 1

    if cont == 1:
        prodb = preco
        maisbarato = prod
    if preco > 1000:
        contp1000 += 1
    if preco < prodb:
        prodb = preco
        maisbarato = prod
    while c not in 'SN':
        c = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
    c = ' '
print(f'O Total gasto foi de R$ {total:.2f}.')
print(f'{contp1000} produtos custam mais do que R$ 1000.00.')
print(f'O produto mais barato é o {maisbarato}.')



