#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
cont = 0
soma = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        cont += n
        soma += 1
print(f'Você digitou {soma} números pares e a sua soma deu {cont}.')