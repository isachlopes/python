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
        