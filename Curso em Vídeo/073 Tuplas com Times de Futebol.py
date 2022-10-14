#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética.  d) Em que posição está o time da Chapecoense.

times = ('Ceará', 'Palmeira', 'Atlético-PR', 'Flamengo', 'São Paulo', 'Chapecoense', 'Bahia', 'Atletico-MG', 'Santos', 'Goiás', 'Corinthians', 'Avaí', 'Grêmio', 'Fluminense', 'Cruzeiro', 'Internacional', 'Botafogo', 'Vasco', 'Fortaleza', 'CSA')
print(times[0:6])
print(times[-4:])
print(sorted(times))
print(f'A équipe da chapecoense está na posição {times.index("Chapecoense" + 1)}.')
