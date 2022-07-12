import math
ca = float(input('Digite o valor do cateto adjascente: '))
co = float(input('Digite o valor do cateto oposto: '))

h= (co**2+ca**2)**(1/2)
hi= math.hypot(co,ca)

print('O Cateto adjascente é {}\nO Cateto oposto é {}\nA Hipotenusa é {:.2f} e no outro metodo {:.2f}'.format(ca,co,h,hi))

