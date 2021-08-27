#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadeM = somaidade = idadeF = 0
nomehvelho = ''
for p in range(1, 5):
    print(f'{"-" * 5} {p}° Pessoa {"-" * 5}')
    nome = str(input('Qual o nome: '))
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        idadeM = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > idadeM:
        idadeM = idade
        nomehvelho = nome
        print(f'O homem mais velho se chama {nome}')
    if sexo == 'F' and idade < 20:
        idadeF += 1
print(f'A media de idade do grupo é {somaidade / p} anos.')
print(f'O homem mais velho se chama {nomehvelho} com {idadeM} anos.')
print(f'Existem {idadeF} menores de 20 anos.')
