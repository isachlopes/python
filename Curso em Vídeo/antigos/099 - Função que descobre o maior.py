#programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.25)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f' O maior valor foi {maior}.')


maior(2, 4, 5, 9, 10, 11)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
