frase = 'Curso em Video Python'
print (frase[::2])
print(frase.count('o')) #le somente 'o' minusculo. (atenção)
print (len(frase)) #conta a quantidade de caracteres ocupados na frase
print( frase.replace('Python','Android')) #substitui as palavras
print ('curso' in frase)  # diz se 'curso' esta na frase (true,-1)
print(frase.lower())

div = frase.split()
print(div [0]) #mostra somente a posição indicada da lista criada


