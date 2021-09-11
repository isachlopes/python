#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matrix = [[],[],[]]
for a in range(0, 3):
    matrix[0].append(int(input(f'Valor para [0, {a}]: ')))
for a in range(0, 3):
    matrix[1].append(int(input(f'Valor para [1, {a}]: ')))
for a in range(0, 3):
    matrix[2].append(int(input(f'Valor para [2, {a}]: ')))
print(matrix)
