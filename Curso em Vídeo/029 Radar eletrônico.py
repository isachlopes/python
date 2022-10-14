#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = int(input('\033[30;42mQual a velocidade do carro?\033[m '))
if speed<= 80:
    print('Você esta trafegando dentro do limite de velocidade.')
else:
    print(f'\033[1;31mMultado!\033[m\nVoce estava trafegando a {speed}km/h, {speed - 80}km/h acima do permitido.\nMulta de R${(speed - 80)*7:.2f}.')