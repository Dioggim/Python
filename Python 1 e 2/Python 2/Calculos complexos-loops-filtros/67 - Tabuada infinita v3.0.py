print('---'*20)
print(f'\033[1;31mTABUADA\033[m')
print('---'*20)
tab = mult = 0
while True:
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        break
    tab = 0
    while tab <= 10:
        mult = n * tab
        print(f'{n} X {tab} = {mult}')
        tab += 1
    print('---'*10)
print('fim')
