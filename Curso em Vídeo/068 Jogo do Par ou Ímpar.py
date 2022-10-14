#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print(f'{"=-" * 10}\nJogando Par ou impar\n{"=-" * 10}')
par_impar = ''
tot = 0
while True:
    n = int(input('Digite um valor: '))
    par_impar = str(input('Par ou Impar?: ')).upper().strip()[0]
    pc = randint(0,10)
    soma = n + pc
    print(f'{"-" * 20}\nVoce jogou {n} e o computador jogou {pc}, total de {soma}. {"Deu par!" if soma % 2 == 0 else "Deu impar!"}\n{"-" * 20}')
    if par_impar == 'P' and soma % 2 == 0 or par_impar == 'I' and soma % 2 == 1:
        print('Você venceu')
        print('Vamos jogar novamente...')
        tot += 1
    elif par_impar == 'P' and soma % 2 == 1 or par_impar == 'I' and soma % 2 == 0:
        print('Você Perdeu!')
        break
print(f'{"=-" * 10}\nGAME OVER! Você venceu {tot} vezes.')
