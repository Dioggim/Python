import datetime
atual = datetime.date.today().year
pess = 1
for pess in range(1,7):
    anon = int(input('Digite o seu ano de nascimento da {} pessoa : '.format(pess)))
    idade = atual - anon
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1

print('De acordo com as datas digitadas, ',end='')
print('temos {} pessoas maiores de 21 anos de idade e {} menores.'.format(maiores, menores))
