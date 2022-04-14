import emoji
print(emoji.emojize('  :Japanese_congratulations_button:'), end ='')
print('\033[1;7;41mBem vindo à Lojinha Xi Jinping\033[m', end='  ')
print(emoji.emojize(':Japanese_congratulations_button:'))
print ('\n\n\033[1;7;41mTemos Diversos produtos e preços especiais!\033[m')
print('                 \033[1;7;46mAproveite!\033[m')
print ('''\n[1] CHAPA QUENTE PLA CACHOLO (Pala voce deixar os pelos do seu cãozinho "na légua")
[2] CABELIN DE NENEM (CREME PARA FAZER CRESCER CABELO EM MARMANJO 30+)
[3] PATINETI (Patinete elétrico com bateria de incríveis 30 segundos, te leva a qualquer lugar!)
[4] FLANGONE (ou Frango Drone Voa baixo e por pouco tempo, mas é divertido)
[5] IPHONE 16 (Não tem nos EUA ainda , mas aqui ja tem Oliginal)
''')
prod = int(input('\nEscolha um produto:'))

prod1 = 'CHAPA QUENTE PLA CACHOLO'
preco1 = 400

prod2 = 'CEBELIN DE NENEM'
preco2 = 100

prod3 = 'PATINETI'
preco3 = 1000

prod4 = 'FLANGONE'
preco4 = 800

prod5 = 'IPHONE 16 Oliginal'
preco5 = 13000

#criando a variavel preco generica e produto generico
if prod == 1:
    prod = prod1
    preco = preco1
elif prod == 2:
    prod = prod2
    preco = preco2
elif prod == 3:
    prod = prod3
    preco = preco3
elif prod == 4:
    prod = prod4
    preco = preco4
elif prod == 5:
    prod = prod5
    preco = preco5
else:
    preco = 0
    print('Você não digitou uma opção válida')

if preco != 0:
    print ('O ploduto escolhido é  o {} e o pleço é de R$ {}'.format(prod,preco))#-------------------------------------------------------------------------------------------------------------
    print ('\n\nTemos diversas formas de pagamento, escolha a ideal para você!')
    print ('[1] à vista débito ou pix com 10 % de desconto\n[2] Cartão de Crédito à vista com 5 % de desconto')
    print ('[3] Cartão de crédito em 2x sem juros\n[4] Parcelamos de 3x à 12x com um pequeno acrescimo de 20 % juros')
    fpag = int(input('Escolha a forma de pagamento: '))

    f1 = '[1] à vista débito ou pix com 10 %'
    f2 = '[2] Cartão de Crédito à vista com 5 % de desconto'
    f3 = '[3] Cartão de crédito em 2x sem juros'
    f4 = '[4] Parcelamos de 3x à 12x com um pequeno acrescimo de 20 % juros'
    #if do produto
    if fpag == 1:
        forma = f1
        precofinal = preco * 0.90
        print('\n\nO produto escolhido é  o {} e a forma de pagamento {}'.format(prod, forma))
        print('O valor do produto é R$ {}, com desconto de 10% será de R$ {} '.format(preco,precofinal))

    elif fpag == 2:
        forma = f2
        precofinal = preco * 0.95
        print('\n\nO produto escolhido é  o {} e a forma de pagamento {}'.format(prod, forma))
        print('O valor do produto é R$ {}, com desconto de 5 % será de R$ {} '.format(preco, precofinal))
    elif fpag == 3:
        forma = f3
        precofinal = preco
        precoparcela = precofinal / 2
        print('\n\nO produto escolhido é  o {} e a forma de pagamento {}.'.format(prod, forma))
        print('O valor do produto é R$ {}, parcelado em 2x ficará em mensais de R$ {} .'.format(preco, precoparcela))
    elif fpag == 4:

        forma = f4
        precofinal = preco * 1.20
        parcelas = int(input('Digite a quantidade de parcelas entre 3 e 12. => '))
        precoparcela = precofinal / parcelas
        print('\n\nO produto escolhido é o {} e a forma de pagamento escolhida foi: {}'.format(prod, forma))
        print('O valor do produto é de R$ {},'.format(preco))
        print('parcelado em {}x ficará em mensais de R$ {}, totalizando R$ {}.'.format(parcelas,precoparcela,precofinal))

    else:
        print('\n\nVocê não digitou uma opção válida')
    #comando opcional: observar a posição das linhas, de acordo com o tab muda a funçao
    #    print('Obligado por visitar a nossa loja!')

#else:
 #   print('Obligado por visitar a nossa loja!')


print('Obligado por visitar a nossa loja!')