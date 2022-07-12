print('=' * 30)
print('{:-^30}'.format('Banco CEV'))
print('=' * 30)
vsac = int(input('Qual o valor a ser sacado: '))
resto = notas = c = 0

while True:
    if (vsac // 50) > 0:
        notas = vsac // 50
        resto = vsac % 50
        print(f'voce receberá {notas} notas de 50 rais.')
        if resto >= 20:
            notas = resto // 20
            resto = resto % 20
            print(f'voce receberá {notas} notas de 20 rais.')
        if resto >= 10:
            notas = resto // 10
            resto = resto % 10
            print(f'voce receberá {notas} notas de 10 real.')
        if resto >= 1:
            notas = resto // 1
            print(f'voce receberá {notas} notas de 1 real.')
        break
    if (vsac // 20) > 0:
        notas = vsac // 20
        resto = vsac % 20
        print(f'voce receberá {notas} notas de 20 rais.')
        if resto >= 10:
            notas = resto // 10
            resto = resto % 10
            print(f'voce receberá {notas} notas de 10 rais.')
        if resto >= 1:
            notas = resto // 1
            resto = resto % 1
            print(f'voce receberá {notas} notas de 1 rais.')
        break
    if (vsac // 1) > 0:
        notas = vsac // 1
        resto = vsac % 1
        print(f'voce receberá {notas} notas de 1 real.')
        break
    else:
        break
print('Fim')


