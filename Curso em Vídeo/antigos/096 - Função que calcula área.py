#Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def medida(largura, altura):
    area = largura * altura
    print(f'A área de um terreno de {largura:.1f}X{altura:.1f} é de {area:.1f}m².')


largura = float(input('Largura(m): '))
altura = float(input('altura(m): '))
medida(largura, altura)
