game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0

while True:
    print('-' *20)
    for c in game:
        print(c)
    print('-' *20)
    print('[a, b, c]\n[d, e, f]\n[g, h, i]')
    print('-' *20)
    cont += 1
    if cont% 2 == 1:
        jog = 1
        print('Vez do jogador 1')
    else:
        jog = -1
        print('Vez do jogador 2')
    posição = ''
    posição = input('Posição: ')
    if posição == 'a':
        game[0][0] = jog
        posição = ''
    if posição == 'b':
        game[0][1] = jog
        posição = ''
    if posição == 'c':
        game[0][2] = jog
        posição = ''
    if posição == 'd':
        game[1][0] = jog
        posição = ''
    if posição == 'e':
        game[1][1] = jog
        posição = ''
    if posição == 'f':
        game[1][2] = jog
        posição = ''
    if posição == 'g':
        game[2][0] = jog
        posição = ''
    if posição == 'h':
        game[2][1] = jog
        posição = ''
    if posição == 'i':
        game[2][2] = jog
        posição = ''
        
    if sum(game[0]) == 3 or sum(game[1]) == 3 or sum(game[2]) == 3 or game[0][0] + game[1][0] + game[2][0] == 3 or game[0][1] + game[1][1] + game[2][1] == 3 or game[0][2] + game[1][2] + game[2][2] == 3 or game[0][0] + game[1][1] + game[2][2] == 3 or game[0][2] + game[1][1] + game[2][0] == 3:
        print('vitória jogador 1')
        break
    if sum(game[0]) == -3 or sum(game[1]) == -3 or sum(game[2]) == -3 or game[0][0] + game[1][0] + game[2][0] == -3 or game[0][1] + game[1][1] + game[2][1] == -3 or game[0][2] + game[1][2] + game[2][2] == -3 or game[0][0] + game[1][1] + game[2][2] == -3 or game[0][2] + game[1][1] + game[2][0] == -3:
        print('vitória jogador 2')
        break
   