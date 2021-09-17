#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
camp = []
gols = []
while True:
    gtotal = 0
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    njogos = int(input(f'Número de jogos de {jogador["nome"]}: '))
    for j in range(0, njogos):
        ngols= int(input(f'Numero de gols na partida {j}: '))
        gtotal += ngols
        gols.append(ngols)
    jogador['jogos'] = gols[:]
    gols.clear()
    jogador['gols'] = gtotal
    camp.append(jogador.copy())
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar:[S/N] ')).upper().strip()[0]
    if continua in 'N':
        break
print('-=' * 35)
print(f'{"Id":<4}{"Nome":<10}{"Gols":<12}{"Total":>12}')
for c in camp:
    for k, v in 
    print(f'{k:<3}{v["nome"]:<10}{v["jogos"]:<12}{v["gols"]:>12}')

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 35)
print(f'O jogador {jogador["nome"]} fez no total {jogador["gols"]} gols')
for cont, j in enumerate(jogador['jogos']):
    print(f'No jogo {cont} o jogador {jogador["nome"]} fez {j} gols.')
print(f'Foi um total de {jogador["gols"]} gols.')