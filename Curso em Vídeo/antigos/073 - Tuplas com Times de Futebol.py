#tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: a) Os 5 primeiros times.
                #b) Os últimos 4 colocados.
                #c) Times em ordem alfabética.
                #d) Em que posição está o time da Chapecoense.
times = ('Ceará', 'Palmeira', 'Atlético-PR', 'Flamengo', 'São Paulo', 'Chapecoense', 'Bahia', 'Atletico-MG',
         'Santos', 'Goiás', 'Corinthians', 'Avaí', 'Grêmio', 'Fluminense', 'Cruzeiro', 'Internacional',
         'Botafogo', 'Vasco', 'Fortaleza', 'CSA')
print('-='*15)
print(f'Times do brisileirão: {times}')
print('-='*15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-='*15)
print(f'os quatro ultimos são: {times[-4:]}')
print('-='*15)
print(f'Em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'A Chapecoence esta em {times.index("Chapecoense")+1}° lugar.')
print('-='*15)