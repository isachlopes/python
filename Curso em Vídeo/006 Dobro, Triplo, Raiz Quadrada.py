#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.
n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = pow(n,(1/2))
print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}. \nE a sua raíz quadrada vale {rq:.3f}.')

