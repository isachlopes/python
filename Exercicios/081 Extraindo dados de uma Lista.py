#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if r == 'N':
        break
lista.sort(reverse=True)
print(f'{"-=" * 20}\nVocê digitou no total {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
   print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')