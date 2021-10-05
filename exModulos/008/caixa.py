#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda
preco = float(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O preço menos 10% é {moeda.moeda(moeda.menos10(preco, 10))}.')
print(f'O preço mais 20% é {moeda.moeda(moeda.mais20(preco, 20))}.')