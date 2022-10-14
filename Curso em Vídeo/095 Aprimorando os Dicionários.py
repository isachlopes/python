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
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(camp):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para!'))
    if busca == 999:
        break
    if busca >= len(camp):
        print(f'Erro! não existe o jogador com o codigo {busca}:')
    else:
        print(f' -- levantamernto do jogador {camp[busca]["nome"]}--')
        for i, g in enumerate(camp[busca]['jogos']):
            print(f'    No jogo {i+1} fez {g} gols!')
    print('-' * 40)
print('Volte sempre!!!!!!!')