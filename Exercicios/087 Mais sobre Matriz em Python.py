#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'posição [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print('-=' * 20)
for l in range(0, 3):
        soma3 += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'A soma dos valores pares é igual a {soma_par}.')
print(f'A soma de elementos na coluna 3 é {soma3}.')
print(f'O maior valor na segunda linha é {maior}')
