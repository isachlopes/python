"""faça um programa que leia um angulo qualquer e mostre na tela o valor do sei seno, cosseno e tangente"""
"""Converter para radianos primeiro"""

from math import sin, cos, tan, radians
a = int(input('digite um angulo: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O seno é {:.4f}, \no cosseno é {:.4f} \ne a tangente é {:.4f}.'.format(seno, cos, tan))


