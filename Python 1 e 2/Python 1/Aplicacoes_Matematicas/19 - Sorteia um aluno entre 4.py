import math
import random

a=input('Digite o nome do primeiro aluno ')
b=input('Digite o nome do segundo aluno ')
c=input('Digite o nome do terceiro aluno ')
d=input('Digite o nome do quarto aluno ')

x= random.choice([a,b,c,d])

print(' Os alunos são {}, {} , {} e {}.'.format(a,b,c,d))

print('O Aluno escolhido foi: {}'.format(x))