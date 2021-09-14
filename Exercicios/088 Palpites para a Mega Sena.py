#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from time import sleep
from random import randint
mega = []
lista = []
njogo = cont = tot = 0
n = int(input('Número de jogos na mega: '))
rand = randint(1, 60)
while True:
    while True:
        if rand not in lista:
            lista.append(rand)
            tot +=1
        if tot >= 6:
            break
    mega.append(lista[:])
    lista.clear()
    cont += 1
    if cont == n:
        break
print(f'{"-=" * 5} Sorteando {n} Jogos{"-=" * 5}')
sleep(1)
for pos, lista in enumerate(mega):
    print(f'jogo {pos + 1} : {lista}')
    sleep(0.3)