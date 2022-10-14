#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print(f'Gerador de PA: \n{"-=" * 8}')
t1 = int(input('digite o primeiro termo: '))
r = int(input('Digita a razão da PA: '))
p = 10
total = 0
#termo = t1
cont = 1 
while p != 0:
    print(f'{t1}', end= ' → ')
    t1 += r
    p -= 1
    total += 1
    if p == 0:
        print('Pausa')
        p = int(input('Quantos termos voce quer mostrar mais: '))
print(f'Foram exibidos {total} termos no total\nFim')