#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior 
# [ 4 ] novos números [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
op = 0
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo Valor: '))
while op !=  5:
    print('-==' *15)
    sleep(1)
    print('''       [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do progama''')
    op = int(input('>>>> Qual a sua opção: '))
    if op == 1:
        print(f'A soma de {v1} e {v2} é igual a {v1 + v2}.')
    elif op == 2:
        print(f'A multiplicação de {v1} e {v2} é igua a {v1 * v2}.')
    elif op == 3:
        if v1 > v2:
            print('O primeiro é maior')
        elif v2 >v1:
            print('O segundo é maior.')
        else:
            print('Os dois são iguais.')
    elif op == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo Valor: '))

print('fim')
