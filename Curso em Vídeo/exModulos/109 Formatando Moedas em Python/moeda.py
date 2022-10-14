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