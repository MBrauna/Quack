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
'''

# Importação de bibliotecas necessárias
import  sqlite3
import  os
import  sys
# Importação de bibliotecas necessárias


# Utilização de recursos de bibliotecas necessárias
from sqlite3 import Error
# Utilização de recursos de bibliotecas necessárias

class mb_sqlite:
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    '''
        Classe de configuração e conexão ao banco de dados através de
    classe sqlite3 e outras bibliotecas de assistência.
        Para toda conexão far-se-à necessária a instalação prévia do
    banco de dados SQLite.

              SQLITE É UM BANCO DE DADOS LEVE E GRATUITO
              VER DOCUMENTAÇÃO E DOWNLOAD ATRAVÉS DO LINK
                       https://www.sqlite.org

    '''

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # # - Variáveis locais da classe MB_SQLITE
    MBRAUNA_CONFIGURACAO            =   None
    MBRAUNA_CONEXAO                 =   None
    # # - Variáveis locais da classe MB_SQLITE

    def __init__(self, p_configuracao):
        '''
        Autor: Michel Brauna                                Data: 12/01/2011

            Classe inicializadora, irá setar as configurações assim como
        inicializar o banco de dados, deixando uma conexão ativa a todo
        instante.
            Para todo inicializador, persistência no banco será realizada.
        '''
        try:
            # Marca a configuração necessária para a inicialização da conexão
            self.MBRAUNA_CONFIGURACAO       =   p_configuracao
            # Marca a configuração necessária para a inicialização da conexão

            # Cria a conexão com o banco de dados SQLite
            MBRAUNA_CONEXAO                 =   sqlite.connect(self.func_caminho())
            MBRAUNA_CONEXAO.isolation_level =   None
            # Cria a conexão com o banco de dados SQLite


        except Exception as e:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
    
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def func_caminho():
        '''
        Autor: Michel Brauna                            Data: 12/01/2011

            Classe para definicao do caminho do banco de dados SQLITE
        '''
        try:
            # Coleta o caminho absoluto do arquivo
            v_tmp_caminho   =   os.getcwd()
            # Coleta o caminho absoluto do arquivo

            return os.path.abspath(os.path.join(v_tmp_caminho,r'./DB/Periscopio.db'))
        except Exception as e:
            return None
    
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
