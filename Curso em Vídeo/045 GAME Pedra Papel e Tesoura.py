#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''SUAS OPÇÕES:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] tesoura''')
voce = int(input('Vou escolher: '))
pc = randint(0,2)
sleep(0.5)
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!!')
print(f'''{12* "-="}
COMPUTADOR JOGOU {itens[pc]}
VOCÊ JOGOU {itens[voce]}
{12* "-="}''')
if pc == 0:
    if voce == 0:
        print('Empate')
    elif voce == 1:
        print('Você Ganhou!')
    
    elif voce == 2:
        print('Computador Ganhou!')
    else:
        print('Opção inválida!')
elif pc == 1:
    if voce == 0:
        print('Computador Ganhou!')
    elif voce == 1:
        print('Empate')
    elif voce == 2:
        print('Você Ganhou!')
    else:
        print('Opção inválida!')
elif pc == 2:
    if voce == 0:
        print('Você Ganhou!')
    elif voce == 1:
        print('Computador Ganhou!')
    elif voce == 2:
        print('Empate')
    else:
        print('Opção inválida!')
