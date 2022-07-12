nome= str(input('digite seu nome completo')).strip()
print('Analisando seu nome...')
print('o seu nome em maiusculas: {}. '.format(nome.upper()))
print('o seu nome em minusculas: {} .'.format(nome.lower()))
print('O seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
x = nome.split()

print('o seu primeiro nome é {} e ele tem {} letras)'.format(x[0], len(x[0])))
