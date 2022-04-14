x= float(input('quanto tem na carteira?'))
dolar = x/ 5.02# na epoca o dalar era essa merreca 3,27
euro = x/5.55
print ('Com R${:.2f} daria para comprar U${:.2f}! Partiu MIAMI, sqn!'.format(x,dolar))
print ('Com R${:.2f} daria para comprar EUR {:.2f}! Partiu ROMA,MAMAMIA, sqn!'.format(x,euro))