alt1 = float(input('Altura da parede 1: '))
larg1 = float(input('Largura da parede 1: '))

Met1 = alt1 * larg1

print ('A parede 1 tem {:.2f} Metros quadrados.'.format(Met1))

alt2 = float(input('Altura da parede 2: '))
larg2 = float(input('Largura da parede 2: '))

Met2 = alt2 * larg2

print ('A parede 2 tem {:.2f} Metros quadrados.'.format(Met2))

com = Met2 * Met1

print ('Temos então um total de {} Metros quadrados de parede neste comodo.'.format(com))

# 1 litro pinta 2 Metros²
Lit= float(com/2)

print ('Sabendo que cada litro de tinta pinta 2 metros quadrados,', end='')
print (' preciso para pintar este comodo? \n {} Litros!'.format(Lit))