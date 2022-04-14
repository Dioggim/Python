s = str(input('Digite o sexo [m/f]: ')).lower().strip()
c = 1
while c == 1:
    if s in 'm':
        print('o sexo digitado foi [{}] Masculino.'.format(s))
        c = 0
    elif s in 'f':
        print('o sexo digitado foi [{}] Feminino.'.format(s))
        c = 0
    else:
        s = str(input('Valor inválido. Digite o sexo com [m] para masculino ou [f] para feminino: ')).strip().lower()

print('Obrigado por usar nosso programa!')
#--------------------------------------------------------
#versao do Guanabara
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0] # esse [0] faz pegar apenas a primeira letra
print('Sexo {} registrado com sucesso.'.format(sexo))