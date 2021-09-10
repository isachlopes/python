#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
pessoa = []
grupo = []
mpesado = mleve = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        mpesado = mleve = pessoa[1]
    else:
        if pessoa[1] > mpesado:
            mpesado = pessoa[1]
        if pessoa[1] < mleve:
            mleve = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    r = input('Continuar?[S/N] ')
    if r in 'Nn':
        break
print(f'Você cadastrou ao todo {len(grupo)} pessoas.')
print(f'O maior peso foi {mpesado}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == mpesado:
        print(f'{p[0]}...', end=' ')
print(f'\nO menor peso foi {mleve}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == mleve:
        print(f'{p[0]}...', end=' ')

