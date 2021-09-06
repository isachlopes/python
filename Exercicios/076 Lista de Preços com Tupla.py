#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(f'{"-" * 40}\n{"COMPRAS ESCOLARES 2021":^40}\n{"-" * 40}\n')
p = ('Lápis', 1.34, 'Caneta', 2.43, 'Caderno', 23.67, 'Mochila', 140.0, 'Estojo', 12.3, 'Borracha', 1.2)
for prod in range(0, len(p)):
    if prod % 2 == 0:
        print(f'{p[prod]:.<30}', end=' ')
    else:
        print(f'R${p[prod]:>7.2f}', end='\n')
print("-" * 40)