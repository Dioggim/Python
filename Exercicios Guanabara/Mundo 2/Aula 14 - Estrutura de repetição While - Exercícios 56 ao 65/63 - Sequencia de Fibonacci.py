print ('Vamos de Fibonacci')
ninicio = int(input('A partir de qual numero quer ver a sequência?'))
nvezes = int(input('Quantas vezes quer ver a sequência?'))
print('O numero escolhido foi {}.'.format(ninicio))
fibo = ninicio
nvezes -= 2
if ninicio == 0:
    fibo = ninicio + 1
print(ninicio, ' => ', fibo, end=' ')
if nvezes >0:
    print(' => ',end ='')
while nvezes > 0:
    if nvezes > 0:
        x = fibo + ninicio
        print(x,' =>',end=' ')
        nvezes -= 1
        if nvezes > 0:
            ninicio = x + fibo
            print(ninicio,' =>',end=' ')
            nvezes -= 1
            if nvezes > 0:
                fibo = ninicio + x
                print(fibo, ' =>', end=' ')
                nvezes -= 1
print('Acabou')

