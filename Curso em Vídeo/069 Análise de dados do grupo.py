#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos. 
mais18 = homens = mulherj = 0
while True:
    idade = int(input('Qual a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o Sexo: [M/F] ')).strip()[0].upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherj += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer Continuar: [S/N] ')).strip()[0].upper()
    if continua == 'N':
        break
print(f'{mais18} pessoas tem mais de 18 anos.\n{homens} homens foram cadastrados.\n{mulherj} mulheres tem menos de 20 anos.')