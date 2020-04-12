#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Qual o nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar?s/n: ').upper()[0]
        if resp in 'SN':
            break
        print('Erro! apenas sim ou não!')
    if resp == 'N':
        break
print('-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para!'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe o jogador com o codigo {busca}:')
    else:
        print(f' -- levantamernto do jogador {time[busca]["nome"]}--')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols!')
    print('-' * 40)
print('Volte sempre!!!!!!!')


