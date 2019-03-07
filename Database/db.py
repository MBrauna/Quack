'''
Autor: Michel Brauna                             Data: 12/01/2011


    ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗ 
    ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
    ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║
    ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║
    ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

'''

# Bibliotecas para conexão ao banco de dados
import os
import psycopg2
import pymysql
import sys
# Bibliotecas para conexão ao banco de dados



class conexao:
    '''
    ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  
    ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
    '''

    DB_CONEXAO      =   None
    DB_VARIAVEIS    =   None

    # Método construtor para MBrauna - Database
    def __init__(self, p_conexao):
        try:
            # Carrega os dados à partir da conexão necessária
            if p_conexao['MB_TIPO']     ==  0:
                self.DB_CONEXAO     =   psycopg2.connect(host       =   p_conexao['MB_HOSPEDEIRO']
                                                        ,port       =   p_conexao['MB_PORTA']
                                                        ,user       =   p_conexao['MB_USUARIO']
                                                        ,password   =   p_conexao['MB_SENHA']
                                                        ,dbname     =   p_conexao['MB_BANCO']
                                                        )
                print('[POSTGRESQL] - Inicialização do banco de dados realizado!')

            elif p_conexao['MB_TIPO']   ==  1:
                self.DB_CONEXAO     =   pymysql.connect(host        =   p_conexao['MB_HOSPEDEIRO']
                                                       ,port        =   p_conexao['MB_PORTA']
                                                       ,user        =   p_conexao['MB_USUARIO']
                                                       ,passwd      =   p_conexao['MB_SENHA']
                                                       ,db          =   p_conexao['MB_BANCO']
                                                       )
                print('[MYSQL] - Inicialização do banco de dados realizado!')
            # Carrega os dados à partir da conexão necessária

            # Salva as variáveis usadas para login
            self.DB_VARIAVEIS       =   p_conexao
            # Salva as variáveis usadas para login

            

        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            # Printa a mensagem de erro
            print('[ERRO] - Ocorreu um erro ao executar INIT DB - [ERRO]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
    # Método construtor para MBrauna - Database

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Função de execução de scripts DDL
    async def executa_DDL(self, p_comando):
        # CREATE TABLE, ALTER TABLE, ETC.
        try:
            # Abre uma sessão no banco de dados
            vtmp_sessao     =   self.DB_CONEXAO.cursor()
            # Abre uma sessão no banco de dados

            # Marca a DDL para execução
            vtmp_sessao.execute(p_comando)
            # Marca a DDL para execução

            # Marca a finalização da sessão
            vtmp_sessao.close()
            # Marca a finalização da sessão

            return True
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            # Printa a mensagem de erro
            print('[ERRO] - Ocorreu um erro ao executar Executa DDL - [ERRO]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')

            return False
    # Função de execução de scripts DDL

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    
    # Função para execução de DML
    def executa_DML(self, p_comando):
        # Insert, Update e Delete
        try:
            # Abre uma sessão no banco de dados
            vtmp_sessao     =   self.DB_CONEXAO.cursor()
            # Abre uma sessão no banco de dados

            # Executa a DDL
            vtmp_sessao.execute(p_comando)
            # Marca a DDL como sucesso

            # Marca o commit
            self.DB_CONEXAO.commit()
            # Marca o commit

            # Marca a finalização da sessão
            vtmp_sessao.close()
            # Marca a finalização da sessão


        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            # Printa a mensagem de erro
            print('[ERRO] - Ocorreu um erro ao executar Executa DML - [ERRO]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
            # Printa a mensagem de erro
    # Função para execução de DML

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Função para execução de CONSULTAS
    def executa_consulta(self, p_comando):
        # Insert, Update e Delete
        try:
            # Abre uma sessão no banco de dados
            vtmp_sessao     =   self.DB_CONEXAO.cursor()
            # Abre uma sessão no banco de dados

            # Executa a DDL
            vtmp_sessao.execute(p_comando)
            # Marca a DDL como sucesso


            # Marca a finalização da sessão
            vtmp_retorno    =   vtmp_sessao.fetchall()
            vtmp_sessao.close()
            # Marca a finalização da sessão

            return vtmp_retorno
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            # Printa a mensagem de erro
            print('[ERRO] - Ocorreu um erro ao executar Executa CONSULTA - [ERRO]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
            # Printa a mensagem de erro
            return None
    # Função para execução de CONSULTAS

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # FUnção para derrubar a conexão ao banco de dados
    def encerra_DB(self):
        try:
            # Marca a finalização da sessão
            self.DB_CONEXAO.close()
            # Marca a finalização da sessão

            return vtmp_retorno
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            # Printa a mensagem de erro
            print('[ERRO] - Ocorreu um erro ao executar Executa CONSULTA - [ERRO]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
            # Printa a mensagem de erro
            return None
    # FUnção para derrubar a conexão ao banco de dados