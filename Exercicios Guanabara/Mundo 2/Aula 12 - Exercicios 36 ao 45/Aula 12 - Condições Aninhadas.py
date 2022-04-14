nome = str(input('Qual é seu nome? '))

if nome == 'Giorgia' or nome == 'Diogo':
    print('Que nome lindo')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é normal')
else:
    print('Seu nome é diferente')

print ('Tenha um bom dia {}'.format(nome))