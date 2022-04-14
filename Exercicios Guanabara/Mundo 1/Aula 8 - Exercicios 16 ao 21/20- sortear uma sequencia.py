import random

n1=input('primeiro: ')
n2=input('segundo: ')
n3=input('terceiro: ')
n4=input('quarto: ')

lista = [n1,n2,n3,n4] #criar lista é uma possibilidade

random.shuffle (lista)

print('A ordem de apresentação será')
print(lista)



