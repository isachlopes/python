#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
preco = float(input('Digite um preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O preço menos 10% é {moeda.menos10(preco, 10, True)}.')
print(f'O preço mais 20% é {moeda.mais20(preco, 20, True)}.')