#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis', 2.00,
            'Caderno', 3.75,
            'Caneta', 0.50,
            'Estojo', 2.35,
            'Mochila', 34.67,
            'Revolver', 123.34,
            'Tiragosto', 23.40)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' *40)
