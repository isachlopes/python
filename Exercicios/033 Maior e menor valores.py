#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor}.\nO maior valor digitado foi {maior}')