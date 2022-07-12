sal = float(input('Digite o salario a ser analisado: '))

print('O salario analisado é de R$ {}'.format(sal))

if sal > 1250:
    nsal = sal*1.10
else:
    nsal= sal*1.15

print('O novo salario com aumento será de R$ {}'.format(nsal))



print ('--=--'*20)
print('''O salario dos funcionarios terão aumentos 
de acordo com as seguintes regras: 
Para salarios superiores a R$ 1250,00 o aumento será de 10%
Para os outros salários até R$ 1250,00 o aumento será de 15%''')
print ('--=--'*20)

