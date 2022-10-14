#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('\033[1;35;43mMe diga um número qualquer:\033[m '))
if num%2 == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é impar.')
