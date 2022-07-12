
vel = int(input('Você é o radar, qual foi a velocidade medida? => '))

if vel <= 80:
    print('Parabéns, sua velocidade é de {}km/h, continue dirigindo com segurança!'.format(vel))
else:
    print('Sua velocidade é de {} km/h, está acima da velocidade permitida 80km/h.'.format(vel))
    print('Sua multa será de R$ 7,00 a cada km/h acima do limite ultrapassado.')
    m = (vel - 80)*7
    print('você ultrapassou a velocidade em {} km/h.'.format(vel-80))
    print('Sua multa terá o valor de R${},00'.format(m))
