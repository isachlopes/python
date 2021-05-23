#O mesmo professor quer sortear a ordem de apresentação do trabalho dos alunos, faça um programa que leia a ordem dos 4 alunos e mostre a ordem na tela.
from random import shuffle
a = input('Digite o nome do aluno 1: ')
b = input('Digite o nome do aluno 2: ')
c = input('Digite o nome do aluno 3: ')
d = input('Digite o nome do aluno 4: ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação é: ')
print(lista)
