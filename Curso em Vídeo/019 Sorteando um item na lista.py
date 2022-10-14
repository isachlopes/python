#Um professor quer sortear para um dos seus quatro alunos para apagar o quadro. faça um programa que leia o nome deles e escrevendo o nome escolhido.

from random import choice
a = input('Digite o nome do aluno 1: ')
b = input('Digite o nome do aluno 2: ')
c = input('Digite o nome do aluno 3: ')
d = input('Digite o nome do aluno 4: ')
lista = [a, b, c, d]
escolhido = choice(lista)
print(f'O aluno escolhido foi o {escolhido}.')
