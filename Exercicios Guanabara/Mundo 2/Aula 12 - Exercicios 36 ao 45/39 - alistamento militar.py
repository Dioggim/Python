import datetime
nas = int(input('Digite o ano do seu nascimento: '))

hoje = datetime.date.today().year

idade = hoje - nas

alistf = 18 - idade

if alistf == 0:
    print('Voce deve se alistar neste ano!')
elif alistf < 1:

    print('Você já deveria ter se alistado hà {} Anos.'.format(int(alistf**2)**(1/2)))
    ano = nas+18
    print('No ano {}'.format(ano))
else:
    ano1 = nas+18
    print ('Você deverá se alistar em {} Anos.'.format(alistf))
    print ('No ano {}.'.format(ano1))


