#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: Mirim')
elif 9 < idade <= 14:
    print('Classificação: Infantil')
elif 14 < idade <= 19:
    print('Classificação:  Junior')
elif 19 < idade <= 25:
    print('Classificação: Sênior')
elif idade > 25:
    print('Classificação: Master')
