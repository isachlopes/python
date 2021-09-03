#programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
games = []
print('-'*30)
print('     SORTEIO MEGA SENA     ')
print('-'*30)
tot = 1
njogos = int(input('Quantos jogos você quer fazer: '))
while tot <= njogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    games.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {njogos} JOGOS ', '-='*3)
for i, l in enumerate(games):
    print(f'Jogo {i +1}: {l}')
    sleep(0.5)
