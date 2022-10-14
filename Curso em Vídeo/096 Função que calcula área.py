#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(c, l):
    areat = c * l
    print(f'A área de un terreno de {c}m x {l}m é de {areat}')
print('----CONTROLE DE TERRENO')
c = float(input('Altura: '))
l = float(input('Largura: '))
area(c, l)

