from modulos.lib import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # escreve um arquivo, se não existir, com esse + vai criar um
        a.close()
    except:
        print('Houve algum erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        a.close
        
        
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dado!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            
