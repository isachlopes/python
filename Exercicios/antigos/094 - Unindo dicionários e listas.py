"""programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
 todos os dicionários em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas
 B) A média de idade
 C) Uma lista com as mulheres
 D) Uma lista de pessoas com idade acima da média"""
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, tente novamente!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar?s/n ').upper()[0]
        if resp in 'SN':
            break
        print('Erro!! Responda S ou N.')
    if resp == 'N':
        break
print(f'a)Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'b)A média de idade é {media:5.2f} anos.')
print(f'c)As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')
print()
print('d) lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Ecerrado')

