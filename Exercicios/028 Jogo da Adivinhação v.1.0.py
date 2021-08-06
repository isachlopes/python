#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
pc = randint(0, 5)
print('-*=' *17)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-*='*17)
gamer = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(1.5)
if gamer == pc:
    print('Parabéns, você conseguiu me vencer!!')
else:
    print(f'Ganhei! Eu pensei no numero {pc} e você no {gamer}!')