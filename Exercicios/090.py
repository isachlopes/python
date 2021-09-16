especie = {}
insecta = []
while True:
    especie['nome'] = input('Nome: ')
    especie['ordem'] = input('Ordem: ')
    especie['praga'] = input('Praga? ').upper().strip()[0]
    insecta.append(especie.copy)
    parar = int(input('Parar:[0] '))
    if parar == 0:
        break

for c in insecta:
    print(c)

    '''print(f'O inseto {c["nome"]} pertence a Ordem {c["ordem"]}. ')
    if c['praga'] == 'S':
        print('É considerado um inseto praga.')
    elif c['praga'] == 'N':
        print('Não é coniderado um inseto praga.')'''


