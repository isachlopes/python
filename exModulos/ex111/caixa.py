#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidades import moeda
preco = float(input('Digite um preço: R$'))
moeda.resumo(preco, 20, 10)