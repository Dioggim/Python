pal = (input('Digite uma frase:')).strip().upper()

print ('Você digitou : {}'.format(pal))
palavras = pal.split()
junto = ''.join (palavras)
inverso = junto[::-1] #entender este comando!!!!!
print(inverso)
