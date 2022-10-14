#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
def maior(* n):
    print('-=' * 20)
    print('Analizando os valores passados...')
    total = top = 0
    for c in n:
        print(c, end=' ')
        if top < c:
            top = c
        total += 1
    print(f'Foram digitados {total} valores ao todo.')
    print(f'O maior valor digitado foi {top}')
maior(6, 4, 2, 1)
maior(1, 4 , 5, 4, 8)
maior()