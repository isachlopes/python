#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
t1 = int(input('digite o primeiro termo: '))
r = int(input('Digita a razão da PA: '))
termo = t1
cont = 0 
while cont <= 10:
    print(f'{termo}', end= ' → ')
    termo += r
    cont += 1
print('fim')