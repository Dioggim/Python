nome = str(input('Qual é o seu nome?  '))
if nome == 'Diogo':
    print('Que nome bonito!')
print('Bom dia, {}!'.format(nome))

#------------------------

n1 = float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(' A sua media foi {:.1f}.'.format(m))

if m>= 7.5:
    print('Sua média foi boa! Parabens!')
else:
    print(' Sua média foi ruim! Estude mais!')
print('----')
print ('Parabens' if m>= 7.5 else 'estude mais')
