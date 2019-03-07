'''
Autor: Michel Brauna                             Data: 12/01/2011


	███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗ 
	████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
	██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║
	██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║
	██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
	╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

              Configuração geral para MBrauna

PARA ALTERAR ALGUMA VARIÁVEL DE AMBIENTE RETIRE A CERQUILHA À FRENTE
DA CONFIGURAÇÃO (#).

'''

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
'''
- Tipos de bancos de dados disponíveis para conexão

[0]	-	PostgreSQL
[1] - 	MySQL
[2]	- 	MongoDB
[3]	-	SQL Server
[4]	-	Oracle
[5]	-	Cassandra
'''
MB_DB_TIPO						=	0
MB_DB_HOSPEDEIRO 				=	'localhost'
MB_DB_PORTA 					=	5432
MB_DB_USUARIO 					=	'postgres'
MB_DB_SENHA 					=	'ABC123abc.'
MB_DB_BANCO 					=	'MBrauna'
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
MB_CHAVE_ACESSO                 =   '8bbd69417c452bf9e1fa2e99d831d43a'
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
MB_RASTREIO_ERRO                =   100
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
MB_DIRETORIO_LOG                =   './log/'
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #