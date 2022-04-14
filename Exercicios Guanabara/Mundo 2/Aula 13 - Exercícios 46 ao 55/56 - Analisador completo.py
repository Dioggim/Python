# homem mais velho
homv = 0
nhomv =''
# mulheres com menos de 20
contm = 0
#media das idades
idadef = 0
midade = 0
for p in range (1,5):
    nome = str(input('Digite o nome da pessoa {}: '.format(p))).strip().capitalize()
    idade = int(input('Digite a idade da pessoa {}:'.format(p)))
    sexo = str(input('Digite o sexo da {} pessoa (m) para masculino ou (f) para feminino: '.format(p))).strip().lower()
    idadef = idadef + idade
    if sexo in 'Mm': #despensa que precise colocar m maiusculo ou minusculo. Nao precisaria ter .lower() na variavel sexo.
        if idade > homv:
            nhomv = nome
            homv = idade
    if sexo == 'f':
        if idade < 20:
            contm = contm + 1
midade = idadef/4
print('O homem mais velho é o {} e tem {} anos.'.format(nhomv,homv))
print('Na lista tivemos {} mulher(es) com menos de 20 anos.'.format(contm))
print('A média das idades declaradas foi {:.2f}'.format(midade))



