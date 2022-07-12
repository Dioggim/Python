import datetime
ano = int(input('Coloque o ano de nascimento do atléta: '))
ano1= datetime.date.today().year
idade = ano1 - ano

print('Idade: {}'. format(idade))

lista = ['MIRIM,INFANTIL,JUNIOR,SÊNIOR,MASTER']

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

print('Dirija-se à sala de sua categoria.')


