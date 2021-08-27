#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
aatual = date.today().year
maiores = 0
menores = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Digite a idade da {pessoa}° pessoa: '))
    iatual = aatual - nasc
    if iatual >=18:
        maiores += 1
    elif iatual < 18:
        menores += 1
print(f'Tivemos {maiores} pessoas maiores de idade e {menores} pessoas menores de idade.')

