#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*n,sit=False):
    """
    Função para analizar as notas de alunos
    :param n: notas de 1 ou mais alunos
    :param sit: indicar ou não a situação do aluno
    :return: dicionario com as possiveis situações
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['média'] >=5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(9.3, 5.6, 4.7, sit=True)
print(resp)
