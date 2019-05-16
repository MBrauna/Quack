'''
#############################################################################
# Autor: Michel Brauna                                     Data: 12/01/2011 #
#############################################################################
#                                                                           #
#  ██████╗ ███████╗██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗  #
#  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██║██╔═══██╗ #
#  ██████╔╝█████╗  ██████╔╝██║███████╗██║     ██║   ██║██████╔╝██║██║   ██║ #
#  ██╔═══╝ ██╔══╝  ██╔══██╗██║╚════██║██║     ██║   ██║██╔═══╝ ██║██║   ██║ #
#  ██║     ███████╗██║  ██║██║███████║╚██████╗╚██████╔╝██║     ██║╚██████╔╝ #
#  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝  #
#      ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗        #
#      ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗       #
#      ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║       #
#      ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║       #
#      ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║       #
#      ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝       #
#                                                                           #
#############################################################################
#                                                                           #
#  Procedimento para leitura, escrita e adição de arquivos para Periscópio  #
#                                                                           #
#############################################################################
'''

# Importação da bibliotecas necessárias para MBrauna Periscópio
import  os
import  sys
# Importação da bibliotecas necessárias para MBrauna Periscópio

class Arquivo(object):
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    VMB_CONFIGURACAO   =   None
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    

    def __init__(self, p_configuracao):
        '''
        #####################################################################
        # Autor: Michel Brauna                             Data: 17/01/2011 #
        #     Procedimento para coleta das informações de configurações     #
        #####################################################################
        '''
        try:
            # Coleta a configuração repassada e adiciona a instância da classe
            self.VMB_CONFIGURACAO   =   p_configuracao
            # Coleta a configuração repassada e adiciona a instância da classe
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
    
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def mb_salva_log()
        try:
            # Verifica se o diretório informado existe #
            if not os.path.exists(self.VMB_CONFIGURACAO['Diretorio']['Log']):
                os.mkdir(self.VMB_CONFIGURACAO['Diretorio']['Log'])

            vquack_log  =   open(self.VMB_CONFIGURACAO['Diretorio']['Log'] + "Periscopio" + strftime("%Y%m%d", gmtime()) +".log", "a+")
            vquack_log.write(strftime("%d/%m/%Y %H:%M:%S", gmtime()) + p_mensagem + '\n')
            vquack_log.close()
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            print('[ALERTA] - Ocorreu um erro ao salvar o log - [ALERTA]\n',p_erro)
            print(ecx_tipo, '\n', ecx_obj, '\n', ecx_dados, '\n', ecx_nome,'\nLinha[',ecx_dados.tb_lineno,']')
    # Método de suporte QUACK - Salva o arquivo na base