#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from time import sleep
from random import randint
mega = []
lista = []
tot = cont = 0
n = int(input('Número de jogos na mega: '))
while cont <= n:
    while True:
        rand = randint(1, 60)
        if rand not in lista:
            lista.append(rand)
            tot += 1
        if tot == 6:
            break
    mega.append(lista[:])
    lista.clear()
    cont += 1
print(f'{"-=" * 5} Sorteando {n} Jogos{"-=" * 5}')
sleep(0.7)
for p, l in enumerate(lista):
    print(f'jogo {p + 1} : {lista}')
    sleep(0.3)