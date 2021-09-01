#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato. 
totpreço = prod1000 = menor = contproduto = 0
nomem = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    totpreço +=preço
    if preço >= 1000:
        prod1000 += 1
    contproduto += 1
    if contproduto == 1 or preço < menor:
        menor = preço
        nomem = produto
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Quer continuar a compra: [S/N]: ')).upper().strip()[0]
    if fim == 'N':
        break
print(f'No final foi gasto no total R${totpreço:.2f}.')
print(f'O total de produtos com valor maior de R$1000 é de {prod1000}.')
print(f'O produto mais barato é o {nomem} que custou R${menor:.2f}.')