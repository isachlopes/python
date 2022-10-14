#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, maior nota, menor nota, média da turma, situação (opcional)
def notas(*nota, sit=False):
    """[summary]
    Args:
        nota: acumulador com as notas de um aluno.
        sit (bool, optional): [quando sit é verdadeiro, vai retornar a sutuação do aluno]. Defaults to False.
    Returns:
        [aluno]: [dicionario com os dados escolares de um aluno]
    """
    aluno = {}
    maior = nota[0]
    menor = nota[0]
    aluno['total'] = len(nota)
    for c in nota:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = sum(nota) / len(nota)
    if sit:
        if aluno['media'] < 5:
            aluno['situação'] = 'Ruim'
        elif 5 <= aluno['media'] < 7:
            aluno['situação'] = 'Razoável'
        elif aluno['media'] >= 7:
            aluno['situação'] = 'Boa'
    return aluno

resp = notas(10, 6, 3, 8, 1, sit=True)
print(resp)
help(notas)