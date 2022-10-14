#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Qual a distância da viagem? '))
if km <200:
    preco = 0.50
else:
    preco = 0.45
print(f'Você esta próximo de começar uma viagem de {km}km.\nE o preço da sua passagem será de R${km*preco:.2f}.')
