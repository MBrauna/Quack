"""
Autor: Michel Brauna                             Data: 12/01/2011

         ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
        ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║   ██║██║   ██║███████║██║     █████╔╝ 
        ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗ 
        ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""



# Bibliotecas para conexão ao banco de dados
import  os
import  psycopg2
import  pymysql
import  sys



from    time                            import gmtime, strftime
# Bibliotecas para conexão ao banco de dados


class quackdb:
    quack_conexao   =   None
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Inicializa o modelo QuackDB - Modelo Quack
    def __init__(self, p_configuracao):
        try:
            # Carrega os dados à partir da conexão necessária
            if p_configuracao['DB']['Tipo']     ==  0:
                self.quack_conexao  =   psycopg2.connect(host       =   p_configuracao['DB']['Hospedeiro']
                                                        ,port       =   p_configuracao['DB']['Porta']
                                                        ,user       =   p_configuracao['DB']['Usuario']
                                                        ,password   =   p_configuracao['DB']['Senha']
                                                        ,dbname     =   p_configuracao['DB']['Banco']
                                                        )

            elif p_configuracao['DB']['Tipo']   ==  1:
                self.quack_conexao  =   pymysql.connect(host        =   p_configuracao['DB']['Hospedeiro']
                                                       ,port        =   p_configuracao['DB']['Porta']
                                                       ,user        =   p_configuracao['DB']['Usuario']
                                                       ,passwd      =   p_configuracao['DB']['Senha']
                                                       ,db          =   p_configuracao['DB']['Banco']
                                                       )
            # Carrega os dados à partir da conexão necessária
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem   =   '[QUACKDB][INIT][ERRO] - Ocorreu um erro ao executar o procedimento [' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro)
            self.quack_arquivo_log(p_configuracao, vtmp_mensagem)
    # Inicializa o modelo QuackDB - Modelo Quack

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # QuackDB - Realiza consulta e retorna o resultado da query
    def realiza_consulta(self, p_configuracao, p_consulta):
        try:
            # Abre uma sessão no banco de dados
            vtmp_sessao     =   self.quack_conexao.cursor()
            # Abre uma sessão no banco de dados

            # Executa a DDL
            vtmp_sessao.execute(p_consulta)
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
            vtmp_mensagem   =   '[QUACKDB][REALIZACONSULTA][ERRO] - Ocorreu um erro ao executar o procedimento [' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro)
            self.quack_arquivo_log(p_configuracao, vtmp_mensagem)
            return None
    # QuackDB - Realiza consulta e retorna o resultado da query

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # QuackDB - Realiza procedimentos no banco de dados
    def executa_procedimento(self, p_configuracao, p_comando):
        try:
            # Abre uma sessão no banco de dados
            vtmp_sessao     =   self.quack_conexao.cursor()
            # Abre uma sessão no banco de dados

            # Executa a DDL
            vtmp_sessao.execute(p_comando)
            # Marca a DDL como sucesso

            # Marca o commit
            p_configuracao['Quack']['DB'].commit()
            # Marca o commit

            # Marca a finalização da sessão
            vtmp_sessao.close()
            # Marca a finalização da sessão

            return True
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem   =   '[QUACKDB][EXECUTAPROCEDIMENTO][ERRO] - Ocorreu um erro ao executar o procedimento [' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro)
            self.quack_arquivo_log(p_configuracao, vtmp_mensagem)
            return False
    # QuackDB - Realiza procedimentos no banco de dados

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Método de suporte QUACK - Procedimento para salvar o arquivo de log
    def quack_arquivo_log(self, p_configuracao, p_mensagem):
        try:
            # Verifica se o diretório informado existe #
            if not os.path.exists(p_configuracao['Diretorio']['Log']):
                os.mkdir(p_configuracao['Diretorio']['Log'])
            vquack_log  =   open(p_configuracao['Diretorio']['Log'] + "QuackLOG" + strftime("%Y%m%d", gmtime()) +".log", "a+")
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