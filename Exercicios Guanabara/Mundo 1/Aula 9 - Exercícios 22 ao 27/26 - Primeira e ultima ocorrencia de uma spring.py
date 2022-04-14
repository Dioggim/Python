frase= str(input('Digite uma frase: ')).upper().strip()
print ('A letra "a" aparece {} vezes'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))