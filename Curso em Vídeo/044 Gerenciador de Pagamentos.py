#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print(f'{15 * "="} Lojas do Isac {15 * "="}')
valor = float(input('Preço das compras(R$): '))
print('''Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
met = int(input('Qual a opção de pagamento:'))
if met == 1:
    print(f'Sua compra de R${valor:.2f} vai custar no final R${valor - valor*(10/100):.2f}')
elif met == 2:
    print(f'Sua compra de R${valor:.2f} vai custar no final R${valor - valor*(5/100):.2f}')
elif met == 3:
    print(f'Sua compra sera parcelada em 2x de {valor / 2}.\nSua compra de R${valor} vai custar no final R${valor:.2f}.')
elif met == 4:
    parcela = int(input('Quantas parcelas?: '))
    print(f'''Sua compra será parcelada em {parcela}x de R${(valor + valor*(20/100))/parcela:.2f} com juros.
Sua compra de R${valor:.2f} vai custar no final R${ valor + valor * (20/100):.2f}''')
