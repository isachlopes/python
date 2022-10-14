def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro! O valor digitado não é um número.\033[m')
            continue
        
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1;31mErro! Você digitou um número não real.\033[m')
            continue
        else:
            return n