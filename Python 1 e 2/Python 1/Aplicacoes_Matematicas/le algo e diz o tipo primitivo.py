n = input('digite algo  ')
print ('numerico:',n.isnumeric())
print ('alfabetico:',n.isalpha())
print ('letra minuscula:',n.islower())
print ('letra maiuscula:',n.isupper())
print ('letra alfanumerico: {}'.format(n.isalnum())) #maneira diferente de fazer
print ('letra capitalizado: {}'.format(n.istitle())) #capitalizado verifica primeira letra se é maiuscula