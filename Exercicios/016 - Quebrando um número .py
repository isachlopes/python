'''crie um programa que leia qualque numero real pelo teclado e mostre na tela a sua porção inteira
from math import trunc
a = float(input('Digite um número: '))
print('O número digitado corresponde a {} e o seu valor inteiro corresponde a {}.'.format(a, trunc(a)))'''

a = float(input('Digite um número: '))
print('O número digitado corresponde a {} e o seu valor inteiro corresponde a {}.'.format(a, int(a)))
