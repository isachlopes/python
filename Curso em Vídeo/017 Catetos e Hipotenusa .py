#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo e calcule o mostre o valor da hipotenuza
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print(f'A hipotenusa equivalente a {hip}.')
