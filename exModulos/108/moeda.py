def dobro(n=0):
    return n * 2

def metade(n=0):
    return n / 2

def menos10(n=0, d=0):
    return n - n * (d / 100)

def mais20(n=0, j=0):
    return n + n * (j / 100)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

