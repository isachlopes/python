#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
n = []
for c in range(0, 5):
    n.append(int(input(f'Digite o valor {c}: ')))
maior = menor = n[0]
for v in n:
    if v > maior:
        maior = v
    if v < menor:
        menor = v
print(f'Você digitou os valores: {n}')
print(f'O maior número digitato foi {maior} e estava nas posições ', end='')
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {menor} e estava nas posições ', end='')
for i, v in enumerate(n):
    if v == menor:
        print(f'{i}...', end='')
