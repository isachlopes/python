#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
game = {}
for n in range(1, 5):
    game[f'jogador{n}'] = randint(1, 6)
for k, v in game.items():
    sleep(0.7)
    print(f'O {k} tirou {v} no dado.')
print('-=' * 40)
ranking = []
ranking = sorted(game.items(), key= itemgetter(1), reverse=True)#o itemgetter vai pegar e vai ordenar pela posição indicada, no caso a 1. foi jogado em outra lista/dicionario, mas podia ser a mesma.
for i, v in enumerate(ranking):#aqui tem que ser tratado como uma lista
    sleep(0.7)
    print(f'{i +1}º Lugar: {v[0]} com {v[1]}')
