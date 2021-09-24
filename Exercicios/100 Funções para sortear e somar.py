#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
lista = []
def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    sleep(0.7)
    for c in range(0, 5):
        a = randint(0, 10)
        lista.append(a)
        print(a, end=' ')
        sleep(0.3)
    lista.sort()
def soma_par(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    sleep(1)
    print(f'\nSomando os valores de {lista}, temos {soma}.')
sorteia(lista)
soma_par(lista)