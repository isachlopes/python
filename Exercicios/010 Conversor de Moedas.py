#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.$=3,27
Real = float(input('Quanto dinheiro você tem na carteira? R$'))
Dolar = Real/3.27
print(f'Com R${Real:.2f} você pode comprar US${Dolar:.2f}')

