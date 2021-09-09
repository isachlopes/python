#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Quer continuar?[S/N] ')
    if r in 'nN':
        break
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)
print(f'A lista conpleta é: {lista}.')
print(f'A lista só com pares é: {lista_par}.')
print(f'A lista dos impares é: {lista_impar}.')