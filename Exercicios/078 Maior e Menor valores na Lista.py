from typing import List


#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
n = []
for c in range(1, 6):
    n.append(int(input(f'Digite o valor {c}: ')))
print(f'Você digitou os valores: {n}')
maior = n[0]
for e, v in enumerate(n):
    if v > maior:
        maior = v
        print(e)
print(maior)