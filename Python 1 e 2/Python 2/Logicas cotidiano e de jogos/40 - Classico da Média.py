nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a primeira nota: '))

m= (nota1+nota2)/2

if m < 5:
    print('Sua nota foi {:.1f} , Você foi Reprovado!'.format(m))
elif m >= 5 and m < 7:
    print ('Sua nota foi {:.1f} ,Você está de Recuperação!'.format(m))
else:
    print ('Sua nota foi {:.1f} , Você passou! Boas Férias'.format(m))
