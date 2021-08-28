print('Faça um programa que leia um número qualquer e mostre o seu fatorial.\n\n\033[32mUsando WHILE\033[m\n')

n = int(input('Diga um número para saber o seu fatorial: '))
cont = n
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(F'{f}')
print('\n\033[32mUsando FOR\033[m\n')
#n = int(input('Diga um número para saber o seu fatorial: '))
cont = n
f = 1
for c in range(n , 0, -1):
    print(c, end=' ')
    f *= c

print(f'\nfatorial de {n} é {f}.')