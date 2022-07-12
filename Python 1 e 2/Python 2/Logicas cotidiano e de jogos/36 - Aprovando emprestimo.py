valc = float(input('Digite o valor da casa: '))
salc = float(input('Seu salário: '))
anoc = int(input('Em quantos anos pretende pagar: '))
print('O valor da casa é R$ {}'.format(valc))
print('O salário é R$ {}\nA pretenção de anos a pagar é {}'.format(salc,anoc))

x = salc * 0.30

print ('O valor minimo de prestação é baseado nos 30% do seu salario R$ {}'.format(x))

mr = (valc/(anoc*12))  #mr mensalidade real = valor da casa dividido pelo tempo em meses
print ('A mensalidade ficaria R$ {}'.format(mr))
if mr>x:
    print('seu empréstimo nao foi aprovado')
else:
    print ('seu empréstimo foi aprovado e sua mensalidade será de : R$ {}'.format(mr))
