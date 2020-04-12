#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
#desenvolvida no desafio 108.


def aumentar(preço=0, taxa=0, formato=False):
    '''
    :param preço: valor do produto
    :param taxa: porcentagem que vai aumentar
    :param formato: formatar no padrao brasileiro
    :return: vai retornar valor res
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')





