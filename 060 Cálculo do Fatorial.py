#Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Diga um número para saber o seu fatorial: '))
cont = n
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f)