#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}.\nOs valores ímpares digitados foram {lista[1]}.')