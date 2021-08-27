#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
n = int(input('digite um numero: '))
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end= '')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('O número \033[30;42mÉ PRIMO!\033[m')
else:
    print('O número \033[0;30;41mNÃO É PRIMO!\033[m')
print('fim')