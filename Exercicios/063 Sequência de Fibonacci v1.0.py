#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
print(f'{"-" * 22}\nSequência de fibonacci\n{"-" * 22}')
t1 = 0
t2 = 1
n = int(input('Quantos elementos você quer mostrar: '))
cont = n
while cont != 0:
    t3 =  t1 + t2
    print(f'{t1}', end= ' → ' )
    t1 = t2
    t2 = t3
    cont -= 1
print('fim')