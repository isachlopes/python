#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
gtotal = 0
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
njogos = int(input(f'Número de jogos de {jogador["nome"]}: '))
for j in range(0, njogos):
    ngols= int(input(f'Numero de gols na partida {j}: '))
    gtotal += ngols
    gols.append(ngols)
jogador['jogos'] = gols
jogador['gols'] = gtotal
print('-=' * 35)
print(jogador)
print('-=' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 35)
print(f'O jogador {jogador["nome"]} fez no total {jogador["gols"]} gols')
for cont, j in enumerate(jogador['jogos']):
    print(f'No jogo {cont} o jogador {jogador["nome"]} fez {j} gols.')
print(f'Foi um total de {jogador["gols"]} gols.')