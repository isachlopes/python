#programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    vai = str(input('Você quer continuar[S/N]?'))
    if vai in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2==0:
        par.append(v)
    else:
        impar.append(v)
print('=-'*30)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {par}.')
print(f'A lista de impares é {impar}.')
