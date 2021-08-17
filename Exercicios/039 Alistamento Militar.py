#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Seu ano de nascimento: '))
ano_atual = date.today().year
idade_atual = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade_atual} em {ano_atual}.')
if idade_atual > 18:
    print(f'Seu alistamento foi a {idade_atual - 18} anos. Você está desde {ano_atual - (idade_atual - 18)} atrasado.')
elif idade_atual == 18:
    print('O seu alistamento é agora! Corre pro quartel!')
elif idade_atual < 18:
    print(f'Ainda faltam {18 - idade_atual} anos para o seu alistamento que será em {ano_atual + (18 - idade_atual)}.')