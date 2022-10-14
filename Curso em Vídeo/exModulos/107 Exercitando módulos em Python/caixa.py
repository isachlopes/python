#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
preco = float(input('Digite um preço: R$'))
print(f' O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}.')
print(f' A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}')
print(f'O preço menos 10% é R${moeda.menos10(preco, 10)}.')
print(f'O preço mais 20% é R${moeda.mais20(preco, 20)}.')