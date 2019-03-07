'''
Autor: Michel Brauna                             Data: 12/01/2011


    ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗ 
    ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
    ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║
    ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║
    ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

'''

# Carrega as bibliotecas para MBrauna Core
import  config
import  os
import  signal
import  sys



from    Database.db                 import conexao
from    time                        import gmtime, strftime
from    Visao.visao                 import visao_mbrauna
# Carrega as bibliotecas para MBrauna Core



class MBrauna:
    '''
    Procedimento para composição do núcleo MBrauna

    ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗ 
    ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
    ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║
    ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║
    ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

                 ██████╗ ██████╗ ██████╗ ███████╗
                ██╔════╝██╔═══██╗██╔══██╗██╔════╝
                ██║     ██║   ██║██████╔╝█████╗
                ██║     ██║   ██║██╔══██╗██╔══╝
                ╚██████╗╚██████╔╝██║  ██║███████╗
                 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    '''

    MB_BANCO_DADOS                  =   {
                                            'MB_TIPO'           :   0
                                           ,'MB_HOSPEDEIRO'     :   '127.0.0.1'
                                           ,'MB_PORTA'          :   0
                                           ,'MB_USUARIO'        :   'xyz'
                                           ,'MB_SENHA'          :   'xyz'
                                           ,'MB_BANCO'          :   'xyz'
                                        }

    MB_VISAO                        =   {
                                            'MB_INSTANCIA'      :   None
                                           ,'MB_CAMERA'         :   [['WebCam',0]]
                                        }

    MB_CONFIGURACAO                 =   {
                                            'MB_CHAVE'          :   '123456'
                                           ,'MB_RASTREIO_ERRO'  :   5
                                           ,'MB_DIRETORIO_LOG'  :   '/var/log'
                                        }
    # Inicialização MBrauna Core -> Procedimento de inicialização
    def __init__(self):
        try:
            # ---------------------------------------------------------------- #
            #  CARREGA AS CONFIGURAÇÕES DO ARQUIVO CONFIG.PY PARA O PROCESSO.  #
            # ---------------------------------------------------------------- #
            # ---------------------------------------------------------------- #
            #      BANCO DE DADOS E SUAS RESPECTIVAS CAMADAS DE EXECUÇÃO       #
            # ---------------------------------------------------------------- #
            # Teste para o tipo de banco de dados
            if self.validaNumerico(config.MB_DB_TIPO) and config.MB_DB_TIPO in (0,1,2,3,4,5):
                self.MB_BANCO_DADOS['MB_TIPO']              =   config.MB_DB_TIPO
            # Teste para o tipo de banco de dados

            # Teste para o endereço do hospedeiro do banco de dados
            if self.validaString(config.MB_DB_HOSPEDEIRO):
                self.MB_BANCO_DADOS['MB_HOSPEDEIRO']        =   config.MB_DB_HOSPEDEIRO
            # Teste para o endereço do hospedeiro do banco de dados

            # Teste para a porta do servidor do banco de dados
            if self.validaNumerico(config.MB_DB_PORTA):
                self.MB_BANCO_DADOS['MB_PORTA']             =   config.MB_DB_PORTA
            # Teste para a porta do servidor do banco de dados

            # Teste para usuário do banco de dados
            if self.validaString(config.MB_DB_USUARIO):
                self.MB_BANCO_DADOS['MB_USUARIO']           =   config.MB_DB_USUARIO
            # Teste para usuário do banco de dados

            # Teste para senha do banco de dados
            if self.validaString(config.MB_DB_SENHA):
                self.MB_BANCO_DADOS['MB_SENHA']             =   config.MB_DB_SENHA
            # Teste para senha do banco de dados

            # Teste para nome do banco de dados
            if self.validaString(config.MB_DB_BANCO):
                self.MB_BANCO_DADOS['MB_BANCO']             =   config.MB_DB_BANCO
            # Teste para nome do banco de dados
            # ---------------------------------------------------------------- #
            #      BANCO DE DADOS E SUAS RESPECTIVAS CAMADAS DE EXECUÇÃO       #
            # ---------------------------------------------------------------- #

            # Inicia a comunicação com o banco de dados
            self.MB_BANCO_DADOS['MB_CONEXAO']               =   conexao(self.MB_BANCO_DADOS)
            # Inicia a comunicação com o banco de dados

            # Inicia o parametro de chave de usuário
            if self.validaString(config.MB_CHAVE_ACESSO):
                self.MB_CONFIGURACAO['MB_CHAVE']            =   config.MB_CHAVE_ACESSO

            if self.validaNumerico(config.MB_RASTREIO_ERRO):
                self.MB_CONFIGURACAO['MB_RASTREIO_ERRO']    =   config.MB_RASTREIO_ERRO
            # INicia o parametro de chave de usuário

            # Parâmetro para salvar log
            if self.validaString(config.MB_DIRETORIO_LOG):
                self.MB_CONFIGURACAO['MB_DIRETORIO_LOG']    =   config.MB_DIRETORIO_LOG
            # ---------------------------------------------------------------- #
            #  CARREGA AS CONFIGURAÇÕES DO ARQUIVO CONFIG.PY PARA O PROCESSO.  #
            # ---------------------------------------------------------------- #

            self.exec_visao()

        except Exception as p_erro:
            # Encerra a conexão com o DB
            self.MB_BANCO_DADOS['MB_CONEXAO'].encerra_DB()
            # Encerra a conexão com o DB
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][INIT][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)
        # Inicialização MBrauna Core -> Procedimento de inicialização


    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #


    # Função para captura do sinal de parada
    def __exit__(self, exc_type, exc_value, traceback):
        # Mais detalhes sobre o erro
        ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
        ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

        vtmp_erro   =   '[CORE][EXIT][MSG][' + ecx_dados.tb_lineno + '] - ' + p_erro
        self.proc_salva_arquivo(vtmp_erro)
        self.MB_BANCO_DADOS['MB_CONEXAO'].encerra_DB()
    # Função para captura do sinal de parada
    # ---------------------------------------------------------------- #
    #                 PROCEDIMENTOS DE SUPORTE AO CORE                 #
    # ---------------------------------------------------------------- #

    # Função para validação de strings, se foram preenchidas ou não
    def validaString(self, p_string):
        try:
            if p_string and p_string is not None and type(p_string) == str and p_string.strip():
                return True
            
            return False
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][VALIDASTRING][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)

            return False
    # Função para validação de strings, se foram preenchidas ou não


    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #


    # Função para validação de numericos, se foram preenchidas ou não
    def validaNumerico(self, p_numerico):
        try:
            if p_numerico and p_numerico is not None and type(p_numerico) in (type(1), type(.1)):
                return True

            return False
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][VALIDANUMERICO][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)
            return False
    # Função para validação de numericos, se foram preenchidas ou não

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Procedure para salvar log dos dados de saída para o arquivo
    def proc_salva_arquivo(self, p_texto):
        try:
            v_caminho       =   self.MB_CONFIGURACAO['MB_DIRETORIO_LOG'] + "MBLOG" + strftime("%Y%m%d%H%M%S", gmtime()) +".log"
            vtmp_arquivo    =   open(v_caminho,"a+")
            vtmp_arquivo.write(p_texto)
            vtmp_arquivo.close()
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            print('[ALERTA] - Ocorreu um erro ao salvar o log - [ALERTA]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
    # Procedure para salvar log dos dados de saída para o arquivo

    # ---------------------------------------------------------------- #
    #                 PROCEDIMENTOS DE SUPORTE AO CORE                 #
    # ---------------------------------------------------------------- #

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # ---------------------------------------------------------------- #
    #                 PROCEDIMENTOS PRINCIPAIS AO CORE                 #
    # ---------------------------------------------------------------- #
    # Coleta de dados da câmera e execução dos procedimentos necessários
    def lista_cameras(self):
        try:
            # Coleta todas as câmeras para execução do pré-processamento de dados
            vtmp_erro   =   '[CORE][LISTA_CAMERAS][MSG] - Inicialização das câmeras token ' + str(self.MB_CONFIGURACAO['MB_CHAVE'])
            self.proc_salva_arquivo(vtmp_erro)

            return self.MB_BANCO_DADOS['MB_CONEXAO'].executa_consulta("select cs.descricao as descricao, cs.url_camera as url, cs.ponto_corte as ponto_corte, cs.id_sistema_camera as id_sistema_camera from sistema s inner join sistema_camera cs on cs.hash_sistema = s.hash where s.hash = '" + str(self.MB_CONFIGURACAO['MB_CHAVE']) + "' and s.ativo = 1 and cs.ativo = 1 order by cs.descricao")
            # Coleta todas as câmeras para execução do pré-processamento de dados
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][LISTA_CAMERAS][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)

            return None
    # Coleta de dados da câmera e execução dos procedimentos necessários

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # executa as imagens enquanto existir informação - MULTIPROCESSING
    def exec_visao(self):
        try:
            # Coleta a lista de câmeras cadastradas para tratamento
            vtmp_camera     =   self.lista_cameras()
            # Coleta a lista de câmeras cadastradas para tratamento

            # Lista de dados para detecção - Câmeras disponíveis
            if vtmp_camera is None or len(vtmp_camera) <= 0:
                vlista_camera       =   [['WebCam',0,50,None]]
            else:
                vlista_camera   =   [[vtmp_camera[curreg][0], vtmp_camera[curreg][1], vtmp_camera[curreg][2],vtmp_camera[curreg][3]]  for curreg in range(len(vtmp_camera))]
            # Lista de dados para detecção - Câmeras disponíveis


            # Inicia a verificação da lista de câmeras para execução
            self.MB_VISAO['MB_INSTANCIA']   =   visao_mbrauna(self.MB_BANCO_DADOS['MB_CONEXAO'],self.MB_CONFIGURACAO)
            self.MB_VISAO['MB_CAMERA']      =   vlista_camera

            try:
                self.MB_VISAO['MB_INSTANCIA'].executa(vlista_camera)
            except Exception as p_erro:
                # Mais detalhes sobre o erro
                ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
                ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

                vtmp_erro   =   '[CORE][EXEC_VISAO|VISAO][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
                self.proc_salva_arquivo(vtmp_erro)

        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[CORE][EXEC_VISAO][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)
    # executa as imagens enquanto existir informação - MULTIPROCESSING

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # ---------------------------------------------------------------- #
    #                 PROCEDIMENTOS PRINCIPAIS AO CORE                 #
    # ---------------------------------------------------------------- #