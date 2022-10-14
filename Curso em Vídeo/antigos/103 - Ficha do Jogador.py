#programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(jog='<desconhecido>', gol=0):
    print(f'o jogador {jog} fez {gol} gols em uma partida.')


n = str(input('Digite o nome do jogador: '))
g = str(input('Quantos gols ele fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
