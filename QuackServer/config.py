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
QUACK_DB_USUARIO        =   'postgres'
QUACK_DB_SENHA          =   'ABC123abc.'
QUACK_DB_BANCO          =   'quackserver'

##########################################################################
#                       CHAVES DE ACESSO AO SISTEMA                      #
##########################################################################
QUACK_CHAVE_SISTEMA     =   'ef52324ea4beda63e1646578dd26e158'

QUACK_ID_USUARIO        =   1
QUACK_CHAVE_USUARIO     =   '230c53159c2a469318eda4ab2c5ace58'

##########################################################################
#              MARGEM DE ERRO DO RASTREIO - POR COORDENADAS              #
##########################################################################
QUACK_MARGEM_RASTREIO   =   100
QUACK_GERA_EXIBICAO     =   False
##########################################################################
#                  DIRETORIO ONDE OS LOGS SERÃO SALVOS                   #
##########################################################################
QUACK_DIRETORIO_LOG     =   './log/'
##########################################################################