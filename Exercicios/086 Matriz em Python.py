#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(0, 3):
    for b in range(0, 3):
        matrix[a][b] = int(input(f'Valor para [{a}, {b}]: '))
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matrix[a][b]:^5}]', end='')
    print()