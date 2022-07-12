dis = int (input('Digite a distancia da viagem: '))
print('voce irá começar uma viagem de {} km.'.format(dis))

val1 = dis * 0.50

val2 = dis * 0.45

if dis <=200:
    print('O valor para esta viagem é de R${:.2f}.'.format(val1))
else:
    print('O valor para esta viagem é de R${:.2f}.'.format(val2))

print ('Boa viagem!')