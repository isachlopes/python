"""
    SCRIPT DESENVOLVIDO PARA LIVE DE PYTHON NO CANAL GEOCURSOS

    - PERCORRE PASTAS IDENTIFICANDO ARQUIVOS ZIP DO CAR (CADASTRO AMBIENTAL RURAL)
        QUE CONTENHAM SHAPEFILES

    - EXTRAI ARQUIVOS ZIPADOS E IMPORTA PARA BASE GPKG

    AUTOR: MARCO AURÉLIO
"""
import os
import io
import shutil
import subprocess
from zipfile import ZipFile, BadZipFile
from datetime import datetime, timedelta
from osgeo import ogr

path = r"C:\Geocursos\Live\Dados\GO"
path_temp = r"C:\Geocursos\Live\Script\temp"
arquivo_saida = r"C:\Geocursos\Live\Script\saida.gpkg"


def limpar_temp(tmp):
    """
    Função para realizar a deleção e criação da pasta temporária

    Parameters:
        arq (string): "Path" do Arquivo gpkg a ser criado
    """
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)

def criar_gpkg(arq):
    """
    Função para realizar a deleção e criação da base de saida.

    Parameters:
        arq (string): "Path" do Arquivo gpkg a ser criado
    """
    driver = ogr.GetDriverByName("GPKG")
    if os.path.exists(arq):
        driver.DeleteDataSource(arq)
    driver.CreateDataSource(arq)

def importar_arquivo_shp(arq, nome_arq, arq_saida):
    """
    Função para realizar a importação do arquivo para a base de saida.

    Parameters:
        arq (string): "Path" do Arquivo Shapefile de entrada
        nome_arq (string): nome do arquivo Shapefile de entrada
        arq_saida (string): Arquivo GPKG de saida
    """

    comando = f'ogr2ogr -f GPKG -append -update -nlt PROMOTE_TO_MULTI -nln "{nome_arq}" '
    comando += f'"{arq_saida}" "{arq}" '

    with subprocess.Popen(comando) as process:
        process.wait()
        process.kill()

def extract(arq):
    """
        Função para realizar a importação do arquivo para a base de saida.

        Parameters:
            arq (string): "Path" do Arquivo gpkg a ser criado
    """
    with ZipFile(arq, 'r') as zip_file:
        for filename in zip_file.namelist():
            content = io.BytesIO(zip_file.read(filename))
            with ZipFile(content, 'r') as subzip_file:
                for i in subzip_file.namelist():
                    subzip_file.extract(i, path_temp)

dt_ini = datetime.now()

limpar_temp(path_temp)
criar_gpkg(arquivo_saida)

cont = 1

for root, folder, files in os.walk(path):
    for file in files:
        # Identifica arquivos ZIP
        if file.endswith('.zip'):
            arquivo = os.path.join(root, file)
            print(cont, arquivo, sep=' - ')

            # Tenta exportar o arquivo
            try:
                extract(arquivo)
            #em caso de erro, printa qual arquivo é e o erro apresentado
            except BadZipFile as error:
                print('-=-=-=-= ARQUIVO INVÁLIDO: "', arquivo, '" - ERRO:', error)

        # percorre pasta temporária que contém arquivos "SHP"
        for root_s, folder_s, files_s in os.walk(path_temp):
            for file_s in files_s:
                # identifica arquivos SHP
                if file_s.endswith('.shp'):
                    # Extrai a extensão do arquivo, deixando somente o nome
                    nome_arquivo_s = file_s[:-4]
                    arquivo_s = os.path.join(root_s, file_s)

                    importar_arquivo_shp(arquivo_s, nome_arquivo_s, arquivo_saida)

        cont += 1

dt_fim = datetime.now()

total = dt_fim - dt_ini

print(timedelta(seconds=total.total_seconds()))
