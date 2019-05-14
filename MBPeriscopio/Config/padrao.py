'''
#####################################################################
# Autor: Michel Brauna                             Data: 12/01/2011 #
#####################################################################
#                                                                   #
#   ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗   #
#   ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗  #
#   ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║  #
#   ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║  #
#   ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║  #
#   ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝  #
#                                                                   #
#  ██████╗ ███████╗██████╗ ██╗███████╗ ██████╗██████╗ ██╗ ██████╗   #
#  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██║██╔═══██╗  #
#  ██████╔╝█████╗  ██████╔╝██║███████╗██║     ██████╔╝██║██║   ██║  #
#  ██╔═══╝ ██╔══╝  ██╔══██╗██║╚════██║██║     ██╔═══╝ ██║██║   ██║  #
#  ██║     ███████╗██║  ██║██║███████║╚██████╗██║     ██║╚██████╔╝  #
#  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝     ╚═╝ ╚═════╝   #
#                                                                   #
#####################################################################
#            Configuração geral para MBrauna periscópio             #
#####################################################################

PARA ALTERAR ALGUMA VARIÁVEL DE AMBIENTE RETIRE A CERQUILHA À FRENTE
DA CONFIGURAÇÃO (#).
'''


##########################################################################
#                    CONFIGURAÇÕES DE BANCO DE DADOS                     #
##########################################################################
'''
- Tipos de bancos de dados disponíveis para conexão local

[0] -   PostgreSQL
[1] -   MySQL
[2] -   MongoDB
[3] -   SQL Server
[4] -   Oracle
[5] -   Cassandra
[6] -   SQLite
'''
MBRAUNA_DB_TIPO             =   0
MBRAUNA_DB_HOSPEDEIRO       =   'localhost'
MBRAUNA_DB_PORTA            =   None
MBRAUNA_DB_USUARIO          =   'periscopio'
MBRAUNA_DB_SENHA            =   'P3r1sc0p10*'
MBRAUNA_DB_BANCO            =   'MBraunaPeriscopio'

# Token para acesso ao banco de dados externo
# Sem essa informação será impossível comunicar qualquer eventualidade.
MBRAUNA_DB_TOKEN            =   ''
# Token para acesso ao banco de dados externo



##########################################################################
#                       CHAVES DE ACESSO AO SISTEMA                      #
##########################################################################
MBRAUNA_USUARIO_TOKEN       =   ''



##########################################################################
#                  DIRETORIO ONDE OS LOGS SERÃO SALVOS                   #
##########################################################################
QUACK_DIRETORIO_LOG     =   './log/'