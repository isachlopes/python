#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def jogador(nome, gols):
    if nome in '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
print('-' * 30)
jog = str(input('Nome do jogador: ')).capitalize()
art = str(input('Quantos gol(s) marcou: '))
print(jogador(jog, art))
