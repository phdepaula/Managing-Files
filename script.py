import os
import logging
from datetime import datetime
from os import path
import shutil


def ler_log(nome_arquivo):
    arquivo = open('./logs/' + nome_arquivo, 'r')
    print(arquivo.read())


def verificar_diretorio():
    diretorios = ['in', 'out', 'bads']
    for tipo in diretorios:
        relacao = os.path.exists(tipo)
        if relacao == False:
            logging.info('Falta diretório!')
            exit()


def analise_arquivo():
    arquivos_dir_in = os.listdir('./in/')
    n = 0

    while n < len(arquivos_dir_in):
        nome_arquivo = arquivos_dir_in[n]
        resultado = 0
        logging.info('')
        logging.info('Processando o arquivo ' + nome_arquivo)
        with open('./in/' + nome_arquivo, 'r') as conteudo:
            texto = conteudo.readlines()
            num_linha = 0
            while num_linha < len(texto):
                linha = texto[num_linha].split()
                for palavra in linha:
                    if palavra == 'chave':
                        resultado = resultado + 1
                num_linha = num_linha + 1
        if resultado > 0:
            logging.info('Chave encontrada!')
            logging.info('Movendo o arquivo...')
            shutil.move('./in/' + nome_arquivo, './out/' + nome_arquivo)
        else:
            logging.info('Chave não encontrada!')
            logging.info('Movendo o arquivo...')
            shutil.move('./in/' + nome_arquivo, './bads/' + nome_arquivo)
        n = n + 1


def start():
    data_atual = datetime.now()
    data_str = data_atual.strftime('%Y%m%d%H%M%S')
    nome_arquivo = "teste_" + data_str + ".log"
    log_file = path.join('./logs/', nome_arquivo)

    logging.basicConfig(level=logging.INFO, filename=log_file, format="%(asctime)s | %(message)s")
    verificar_diretorio()
    logging.info('Iniciando o processamento')
    analise_arquivo()
    ler_log(nome_arquivo)


start()
