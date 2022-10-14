#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')


def leiaint(msg):
    global n
    while True:
        n = str(input(msg))
        if n.isnumeric():
            break
        else:
            print(f'\033[1;31mErro! O valor digitado não é um número.\033[m')


leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')