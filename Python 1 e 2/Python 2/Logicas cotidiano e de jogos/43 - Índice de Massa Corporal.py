peso = float(input('Digite seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso/ (altura**2)
print ('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Voce está abaixo do peso!')
elif 18.5 <= imc <=25:
    print('Voce está na faixa  de peso normal!')
elif 25 <= imc < 30:
    print ('Você está com sobrepeso!')
elif 30 <= imc <= 40:
    print ('Você tem Obesidade')
else:
    print ('Você tem Obesidade Morbida')