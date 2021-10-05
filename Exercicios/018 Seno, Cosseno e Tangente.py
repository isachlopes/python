#faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente
#Converter para radianos primeiro

from math import sin, cos, tan, radians
a = int(input('digite um angulo: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print(f'O seno é {seno:.4f}, \no cosseno é {cos:.4f} \ne a tangente é {tan:.4f}.')
