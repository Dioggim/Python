pal = (input('Digite uma frase:')).strip().upper()

print ('Você digitou : {}'.format(pal))
palavras = pal.split()
junto = ''.join (palavras)
inverso = ''

for letra in range (len(junto)-1,-1,-1):
    #inverso += junto[letra]
    inverso = inverso + junto [letra]
    print ('=>',inverso)
print ('O inverso de {}, é {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não temos um Palíndromo.')

#--------------------------------------------------------------------
pal = (input('Digite uma frase:')).strip().upper()

print ('Você digitou : {}'.format(pal))
palavras = pal.split()
junto = ''.join (palavras)
inverso = junto[::-1]
print(inverso)
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não temos um Palíndromo.')