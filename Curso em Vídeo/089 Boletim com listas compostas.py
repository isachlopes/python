#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
aluno = []
notas = []
continua = ''
while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    notas.append(aluno[:])
    aluno.clear()
    continua = str(input('Continua?[S/N] ')).upper().strip()[0]
    if continua in 'N':
        break
print('-=' * 20)
print(f'{"id":<4}{"Nome":<10}{"Média":>8}')
print('-' * 22)
for n, aluno in enumerate(notas):
    print(f'{n:<4}', end='')
    print(f'{aluno[0]:<10}', end='')
    print(f'{aluno[3]:>8}')
print('-' * 22)
while True:
    ver_notas = int(input('id Aluno:[999 para parar] '))
    if ver_notas == 999:
        break
    print(f'notas do aluno {notas[ver_notas][0]}: {notas[ver_notas][1:3]}')
    print('-' * 20)