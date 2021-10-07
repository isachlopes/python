def moneyread(n):
    valido = False
    while not valido:
        c = str(input(n)).replace(',', '.').strip()
        if c.isalpha() or c == '':
            print(f'\033[1;31mERRO: "{c}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(c)
