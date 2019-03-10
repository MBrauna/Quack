'''
Autor: Michel Brauna                             Data: 12/01/2011

         ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
        ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║   ██║██║   ██║███████║██║     █████╔╝ 
        ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗ 
        ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

              Configuração geral para Quack

PARA ALTERAR ALGUMA VARIÁVEL DE AMBIENTE RETIRE A CERQUILHA À FRENTE
DA CONFIGURAÇÃO (#).

'''

##########################################################################
#                    CONFIGURAÇÕES DE BANCO DE DADOS                     #
##########################################################################
'''
- Tipos de bancos de dados disponíveis para conexão

[0] -   PostgreSQL
[1] -   MySQL
[2] -   MongoDB
[3] -   SQL Server
[4] -   Oracle
[5] -   Cassandra
'''
QUACK_DB_TIPO           =   0
QUACK_DB_HOSPEDEIRO     =   'localhost'
QUACK_DB_PORTA          =   5432
QUACK_DB_USUARIO        =   'Quack'
QUACK_DB_SENHA          =   'QuackServer'
QUACK_DB_BANCO          =   'QuackDB'

##########################################################################
#                       CHAVES DE ACESSO AO SISTEMA                      #
##########################################################################
QUACK_CHAVE_ACESSO      =   'ee11006d08568a0fd0512fe2b6f1cac7'
QUACK_CHAVE_USUARIO     =   'ee11006d08568a0fd0512fe2b6f1cac7'
QUACK_ID_USUARIO        =   1

##########################################################################
#              MARGEM DE ERRO DO RASTREIO - POR COORDENADAS              #
##########################################################################
QUACK_MARGEM_RASTREIO   =   100

##########################################################################
#                  DIRETORIO ONDE OS LOGS SERÃO SALVOS                   #
##########################################################################
QUACK_DIRETORIO_LOG     =   './log/'
##########################################################################