#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).capitalize()
aluno['media'] = float(input('Média: '))
if aluno['media'] < 3:
    aluno['situação'] = 'Reprovado'
elif 3 <= aluno['media'] < 7:
    aluno['situação'] = 'Em Recuperação'
elif 7 <= aluno['media'] <= 10:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')
