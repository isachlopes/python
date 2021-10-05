#Faça um algoritmo que leia o preço de um produto, e mostre o seu novo preço com 5% de desconto.
p = float(input('Digite o valor de um produto: R$'))
d = (p*0.95)
#pode ser assim tbm -- desconto = preço - (preço*5/100)
print(f'O produto que custava R${p:.2f}, com 5% de desconto passa a custar R${d:.2f}.')
