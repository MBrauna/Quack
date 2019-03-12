"""
Autor: Michel Brauna                             Data: 12/01/2011

         ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
        ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║   ██║██║   ██║███████║██║     █████╔╝ 
        ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗ 
        ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

# Carrega as bibliotecas para MBrauna Core
import  config
import  os
import  signal
import  sys



from    Database.quackdb                import  quackdb
from    Visao.quackvisao                import  visao
from    time                            import  gmtime, strftime
# Carrega as bibliotecas para MBrauna Core










class quackserver:
    # Declaração de variáveis globais da aplicação
    QUACK_CONFIG    =   {
                            #######################################
                            # Regras de conexão ao banco de dados #
                            #######################################
                            'DB'        :   {
                                                'Tipo'          :   0
                                               ,'Hospedeiro'    :   'localhost'
                                               ,'Porta'         :   5432
                                               ,'Banco'         :   'quack'
                                               ,'Usuario'       :   'quackserver'
                                               ,'Senha'         :   'Qu4ck!s3rv3r!'
                                            }
                            #######################################
                            #    Instâncias para uso em Quack.    #
                            #######################################
                           ,'Quack'     :   {
                                                'DB'            :   None
                                               ,'Visao'         :   None
                                            }
                            #######################################
                            #  Lista de valores globais de query  #
                            #######################################
                           ,'Lista'     :   {
                                                'Camera'        :   [
                                                                        # Estrutura dos dados de câmera serão
                                                                        # [0] - Nome da câmera
                                                                        # [1] - Endereço da câmera
                                                                        # [2] - Ponto de corte
                                                                        ['WebCam Local',0,50]
                                                                    ]
                                                # Lista de elementos que serão detectados.
                                               ,'Elementos'     :   []
                                            }
                            #######################################
                            #  Chaves de acesso ao sistema Quack  #
                            #######################################
                           ,'Chave'     :   {
                                                'Acesso'        :   'abcdefghijklmnopqrstuvwxyz'
                                               ,'ID'            :   0
                                               ,'Sistema'       :   'abcdefghijklmnopqrstuvwxyz'
                                            }
                            #######################################
                            #              Diretório              #
                            #######################################
                           ,'Diretorio' :   {
                                                'Log'           :   './'
                                            }
                        }
    # Declaração de variáveis globais da aplicação



    """
    Procedimento para composição do núcleo Quack Server

         ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗       
        ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝       
        ██║   ██║██║   ██║███████║██║     █████╔╝        
        ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗        
        ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗       
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       
                                                         
        ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
        ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
        ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
        ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
        ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝

    """

    # Método de inicialização Quack Server - __INIT__
    def __init__(self):
        # Carrega as configurações para QUACK
        try:
            # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

            # Validações necessárias para composição dos dados do banco de dados

            # Para o tipo de DB - Apresentação e teste dos dados numéricos
            if self.valida_Numerico(config.QUACK_DB_TIPO) and config.QUACK_DB_TIPO in (0,1):
                """
                - Tipos de bancos de dados disponíveis para conexão

                [0] -   PostgreSQL
                [1] -   MySQL
                [2] -   MongoDB
                [3] -   SQL Server
                [4] -   Oracle
                [5] -   Cassandra
                """
                self.QUACK_CONFIG['DB']['Tipo']          =   config.QUACK_DB_TIPO
            # Para o tipo de DB - Apresentação e teste dos dados numéricos

            # Para o Hospedeiro do DB - Apresentação e teste dos dados alfanuméricos
            if self.valida_alfanumerico(config.QUACK_DB_HOSPEDEIRO):
                self.QUACK_CONFIG['DB']['Hospedeiro']    =   config.QUACK_DB_HOSPEDEIRO
            # Para o Hospedeiro do DB - Apresentação e teste dos dados alfanuméricos

            # Para a porta do DB - Apresentação e teste dos dados numéricos
            if self.valida_Numerico(config.QUACK_DB_PORTA):
                self.QUACK_CONFIG['DB']['Porta']         =   config.QUACK_DB_PORTA
            # Para a porta do DB - Apresentação e teste dos dados numéricos

            # Para a schemma do DB  - Apresentação e teste dos dados alfanuméricos
            if self.valida_alfanumerico(config.QUACK_DB_BANCO):
                self.QUACK_CONFIG['DB']['Banco']         =   config.QUACK_DB_BANCO
            # Para a schemma do DB  - Apresentação e teste dos dados alfanuméricos

            # Para o usuário do DB - Apresentação e testes dos dados alfanuméricos
            if self.valida_alfanumerico(config.QUACK_DB_USUARIO):
                self.QUACK_CONFIG['DB']['Usuario']       =   config.QUACK_DB_USUARIO
            # Para o usuário do DB - Apresentação e testes dos dados alfanuméricos

            # Para a senha do DB - Apresentação e testes dos dados alfanuméricos
            if self.valida_alfanumerico(config.QUACK_DB_SENHA):
                self.QUACK_CONFIG['DB']['Senha']         =   config.QUACK_DB_SENHA
            # Para a senha do DB - Apresentação e testes dos dados alfanuméricos

            # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

            # Validações necessárias para composição das chaves do sistema

            # Para chave de acesso de acesso ao sistema QUACK
            if self.valida_alfanumerico(config.QUACK_CHAVE_SISTEMA):
                self.QUACK_CONFIG['Chave']['Sistema']    =   config.QUACK_CHAVE_SISTEMA
            # Para chave de acesso de acesso ao sistema QUACK

            # Para ID do usuário de acesso ao sistema QUACK
            if self.valida_Numerico(config.QUACK_ID_USUARIO):
                self.QUACK_CONFIG['Chave']['ID']         =   config.QUACK_ID_USUARIO
            # Para ID do usuário de acesso ao sistema QUACK

            # Para chave de acesso do usuário ao sistema QUACK
            if self.valida_alfanumerico(config.QUACK_CHAVE_USUARIO):
                self.QUACK_CONFIG['Chave']['Acesso']     =   config.QUACK_CHAVE_USUARIO
            # Para chave de acesso do usuário ao sistema QUACK

            # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

            # Validações necessárias para composição dos diretórios

            # Para caminho do diretório de log - Quack
            if self.valida_alfanumerico(config.QUACK_DIRETORIO_LOG):
                self.QUACK_CONFIG['Diretorio']['Log']   =   config.QUACK_DIRETORIO_LOG
            # Para caminho do diretório de log - Quack
            # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
        except Exception as p_erro:
            vtmp_mensagem   =   '[QUACKSERVER][CONFIG]['+ str(ecx_dados.tb_lineno) + '] - Não foi possível o carregamento das configurações! Verifique.' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_mensagem)
            sys.exit()
        # Carrega as configurações para QUACK

        # Consulta externamente os dados para composição do QuackServer
        try:
            # Inicializa o DB
            if not self.inicializacao_DB():
                raise ValueError('[QUACKSERVER][CONFIG][DB] Não foi possível carregar o banco de dados! Verifique.')

            if self.QUACK_CONFIG['Quack']['DB'] is None:
                raise ValueError('[QUACKSERVER][CONFIG][DB] Não foi possível carregar o banco de dados! Verifique.')

            if not self.inicializacao_visao():
                raise ValueError('[QUACKSERVER][CONFIG][VISAO] Não foi possível carregar Quack Visao! Verifique.')

            if self.QUACK_CONFIG['Quack']['Visao'] is None:
                raise ValueError('[QUACKSERVER][CONFIG][VISAO] Não foi possível carregar Quack Visao! Verifique.')
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            vtmp_mensagem   =   '['+ str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_mensagem)
            sys.exit()
        except ValueError as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            vtmp_mensagem   =   '['+ str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_mensagem)
            sys.exit()
        # Consulta externamente os dados para composição do QuackServer
    # Método de inicialização Quack Server - __INIT__

    # --------------------------------------------------------------- #

    # Método de suporte QUACK - Validação de dados numéricos
    def valida_Numerico(self, p_valor):
        try:
            if p_valor and p_valor is not None and type(p_valor) in (type(1), type(.1)):
                return True

            return False
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][VALIDANUMERICO][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)
            return False
    # Método de suporte QUACK - Validação de dados numéricos

    # --------------------------------------------------------------- #

    # Método de suporte QUACK - Validação de dados alfanuméricos
    def valida_alfanumerico(self, p_valor):
        try:
            if p_valor and p_valor is not None and type(p_valor) == str and p_valor.strip():
                return True
            
            return False
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][VALIDAALFANUMERICO][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)

            return False
    # Método de suporte QUACK - Validação de dados alfanuméricos

    # --------------------------------------------------------------- #

    # Método de suporte QUACK - Procedimento para salvar o arquivo de log
    def quack_arquivo_log(self, p_mensagem):
        try:
            # Verifica se o diretório informado existe #
            if not os.path.exists(self.QUACK_CONFIG['Diretorio']['Log']):
                os.mkdir(self.QUACK_CONFIG['Diretorio']['Log'])

            vquack_log  =   open(self.QUACK_CONFIG['Diretorio']['Log'] + "QuackLOG" + strftime("%Y%m%d", gmtime()) +".log", "a+")
            vquack_log.write(strftime("%d/%m/%Y %H:%M:%S", gmtime()) + p_mensagem + '\n')
            vquack_log.close()
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            print('[ALERTA] - Ocorreu um erro ao salvar o log - [ALERTA]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
    # Método de suporte QUACK - Procedimento para salvar o arquivo de log

    # --------------------------------------------------------------- #

    # Inicialização do DB - QuackDB
    def inicializacao_DB(self):
        # Carrega a lista de informações
        try:
            self.QUACK_CONFIG['Quack']['DB']    =   quackdb(self.QUACK_CONFIG)
        except Exception as p_erro:
            vtmp_mensagem                       =   '[QUACKSERVER][INICIALIZACAODB] - Não foi possível inicializar o banco de dados em ' + strftime("%d/%m/%Y %H:%M:%S", gmtime()) + '\n [ERRO DB] ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            vtmp_retorno                        =   False
        else:
            vtmp_mensagem                       =   '[QUACKSERVER][INICIALIZACAODB] - Banco de dados inicializado em ' + strftime("%d/%m/%Y %H:%M:%S", gmtime())
            vtmp_retorno                        =   True
        finally:
            self.quack_arquivo_log(vtmp_mensagem)
            return vtmp_retorno
    # Inicialização do DB - QuackDB

    # --------------------------------------------------------------- #

    # Inicialização da visão - QuackDB
    def inicializacao_visao(self):
        # Carrega a lista de informações
        try:
            self.QUACK_CONFIG['Quack']['Visao']    =   visao(self.QUACK_CONFIG)
        except Exception as p_erro:
             # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem                           =   '[QUACKSERVER][INICIALIZACAOVISAO][' + str(ecx_dados.tb_lineno) + ']  - Não foi possível inicializar a visão! ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            vtmp_retorno                            =   False
        else:
            vtmp_mensagem                           =   '[QUACKSERVER][INICIALIZACAOVISAO] - Visão inicializada'
            vtmp_retorno                            =   True
        finally:
            self.quack_arquivo_log(vtmp_mensagem)
            return vtmp_retorno
    # Inicialização da visão - QuackDB

    # --------------------------------------------------------------- #

    # Consulta todos os dados de câmeras, caso exista - Se não existir ... seta o filtro padrão
    def lista_cameras(self):
        try:
            vtmp_consulta   =   "select c.nome as nome_cliente ,c.nome_fantasia as nome_fantasia ,c.chave_acesso as cliente_chave ,sa.chave_acesso as sistema_chave, s.id_sistema as id_sistema ,s.descricao as sistema_descricao ,sa.id_sistema_acesso as id_sistema_acesso ,la.id_lista_camera as id_lista_camera ,la.url_camera as url_camera ,la.ponto_corte as ponto_corte from cliente c inner join sistema_acesso sa on sa.id_cliente = c.id_cliente inner join sistema s on s.id_sistema = sa.id_sistema inner join lista_camera la on la.id_sistema_acesso = sa.id_sistema_acesso where s.ativo = 1 and sa.situacao = 1 and la.situacao = 1 and c.id_cliente = '" + str(self.QUACK_CONFIG['Chave']['ID']) + "' and c.chave_acesso = '" + str(self.QUACK_CONFIG['Chave']['Acesso']) + "' and sa.chave_acesso = '" + str(self.QUACK_CONFIG['Chave']['Sistema']) + "'"
            vtmp_resultado  =   self.QUACK_CONFIG['Quack']['DB'].realiza_consulta(self.QUACK_CONFIG, vtmp_consulta)

            if vtmp_resultado is not None:
                self.QUACK_CONFIG['Lista']['Camera']    =   vtmp_resultado

            return True
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem   =   '[QUACKSERVER][LISTACAMERA][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_mensagem)
            return False
    # Consulta todos os dados de câmeras, caso exista - Se não existir ... seta o filtro padrão



    # ---------------------------------------------------------------- #
    #             PROCEDIMENTOS PRINCIPAIS AO QUACK SERVER             #
    # ---------------------------------------------------------------- #

    # Método de execução para QuackServer - Inicializa a visão e separa os canais
    def executa_quack(self):
        try:
            # Marca que as câmeras que serão utilizadas
            self.lista_cameras()
            # Marca que as câmeras que serão utilizadas

            # Lista de dados para detecção - Câmeras disponíveis

            # Lista de dados para detecção - Câmeras disponíveis
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem   =   '[QUACKSERVER][EXECUTAQUACK][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_mensagem)
    # Método de execução para QuackServer - Inicializa a visão e separa os canais


    # ---------------------------------------------------------------- #
    #             PROCEDIMENTOS PRINCIPAIS AO QUACK SERVER             #
    # ---------------------------------------------------------------- #