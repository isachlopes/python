#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Informe um número: '))
print(f'Analizando o número {n}:')
print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')
