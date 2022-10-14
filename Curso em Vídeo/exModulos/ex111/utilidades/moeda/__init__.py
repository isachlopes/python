def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)

def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)

def menos10(n=0, d=0, formato=False):
    res = n - n * (d / 100)
    return res if formato is False else moeda(res)

def mais20(n=0, j=0, formato=False):
    res = n + n * (j / 100)
    return res if formato is False else moeda(res)
 
def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n=0, j=20, d=10):
    print(f'{"-" * 32}\n{"RESUMO DO VALOR".center(32)}\n{"-" * 32}\n')
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Preço menos 10%: \t{menos10(n, d, True)}')
    print(f'Preço mais 20%: \t{mais20(n, j, True)}')
    print(f'{"-" * 32}')