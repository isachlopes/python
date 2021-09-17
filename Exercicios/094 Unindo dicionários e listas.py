#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
from operator import itemgetter
pessoa = {}
grupo = []
soma_idade = 0
while True:
    pessoa['sexo'] = ' '
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar:[S/N] ')).upper().strip()[0]
    grupo.append(pessoa.copy())
    if continua in 'N':
        break
print('-=' * 35)
print(f'A) Foram cadastradas {len(grupo)} pessoas.')
media = soma_idade / len(grupo)
print(f'B) A media de idade foi {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) As pessoas com idade acima da media são: ', end='')
for p in grupo:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
