#programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Qual o nome: ')))
    temp.append(float(input('Qual o peso: ')))
    if len(princ)== 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            maior = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar?[S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f' o mair peso foi {maior}Kg. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'o menor peso foi {menor}. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
