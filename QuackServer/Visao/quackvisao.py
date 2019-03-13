"""
Autor: Michel Brauna                             Data: 12/01/2011

         ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗
        ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║   ██║██║   ██║███████║██║     █████╔╝ 
        ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗ 
        ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

# Bibliotecas externas para reconhecimento facial
import  base64                                                                                          ## Biblioteca para tratamento em base64
import  cv2                                                                                             ## Biblioteca para leitura de câmeras e detecção
import  PIL.Image                                                       as Imagem                       ## Biblioteca para tratamento de imagens
import  numpy                                                           as np
import  os
import  sys
import  tensorflow                                                      as tf




from    .Identifica.utils               import  label_map_util          as cx_desc                      ## Biblioteca para geração do texto nas imagens
from    .Identifica.utils               import  visualization_utils     as visualizacao                 ## Biblioteca para visualização dos textos
from    threading                       import Thread
from    time                            import gmtime, strftime
# Bibliotecas externas para reconhecimento facial




os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''
0 = Todas as mensagens são exibidas
1 = Mensagens informativas não são exibidas
2 = Mensagens informativas e avisos não são exibidas
3 = Mensagens informativas, avisos e erros não são exibidas
'''

class visao:
    """
    FONT_HERSHEY_SIMPLEX = 0,
    FONT_HERSHEY_PLAIN = 1,
    FONT_HERSHEY_DUPLEX = 2,
    FONT_HERSHEY_COMPLEX = 3,
    FONT_HERSHEY_TRIPLEX = 4,
    FONT_HERSHEY_COMPLEX_SMALL = 5,
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
    FONT_HERSHEY_SCRIPT_COMPLEX = 7,
    FONT_ITALIC = 16
    """
    QUACK_FONTE                             =   cv2.FONT_HERSHEY_DUPLEX
    # # --------------------------------------------------------------# #
    # #                    VARIAVEL INTERNA - ARRAY                   # #
    # # --------------------------------------------------------------# #
    QUACK_COR                               =   []
    QUACK_MODELO_TF                         =   []
    QUACK_MODELO_FACIAL                     =   []
    QUACK_CONFIG                            =   {}
    QUACK_EXTENSAO                          =   [
                                                    # Imagem - Extensões de imagem
                                                    '.art'
                                                   ,'.bmp'
                                                   ,'.cgm'
                                                   ,'.cin'
                                                   ,'.dpx'
                                                   ,'.dxf'
                                                   ,'.exr'
                                                   ,'.fpx'
                                                   ,'.gif'
                                                   ,'.jpeg'
                                                   ,'.jpg'
                                                   ,'.pbm'
                                                   ,'.pcd'
                                                   ,'.pgm'
                                                   ,'.pict'
                                                   ,'.png'
                                                   ,'.ppm'
                                                   ,'.svg'
                                                   ,'.tif'
                                                   ,'.tiff'
                                                   ,'.wmf'
                                                   ,'.xbm'
                                                   ,'.xpm'
                                                   # Vídeo - Extensão de vídeos
                                                   ,'.3gp'
                                                   ,'.amr'
                                                   ,'.avi'
                                                   ,'.flac'
                                                   ,'.m4v'
                                                   ,'.mp4'
                                                   ,'.oga'
                                                   ,'.ogg'
                                                   ,'.ogm'
                                                   ,'.opus'
                                                   ,'.wav'
                                                   ,'.webm'
                                                   ,'ogv'
                                                ]
    # # --------------------------------------------------------------# #

    # # --------------------------------------------------------------# #
    # #                    VARIAVEL INTERNA - TUPLA                   # #
    # # --------------------------------------------------------------# #
    QUACK_FACIAL                            =   {
                                                    'OLHO'                  :   {
                                                                                    'OLHO'                  :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Olhos/Olhos.xml')
                                                                                    #,'OLHO_ESQUERDO'         :   os.path.join(r'Deteccao/Biblioteca/haarcascades/Olhos/Olho_esquerdo.xml')
                                                                                    #,'OLHO_DIREITO'          :   os.path.join(r'Deteccao/Biblioteca/haarcascades/Olhos/Olho_direito.xml')
                                                                                }
                                                   ,'OLHO_OCULOS'           :   {
                                                                                    'OCULOS'                :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Olhos/Oculos.xml')
                                                                                }
                                                   ,'SORRISO'               :   {
                                                                                    'SORRISO'               :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Sorriso/Sorriso.xml')
                                                                                }
                                                   ,'HUMANO'                :   {
                                                                                    'ROSTO'                 :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Humano/Rosto.xml')
                                                                                   ,'ROSTO_FRENTE'          :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Humano/Rosto_frente.xml')
                                                                                   ,'ROSTO_ANTIGO'          :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Humano/Rosto_antigo.xml')
                                                                                   ,'ROSTO_PADRAO'          :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Humano/Rosto_padrao.xml')
                                                                                   ,'ROSTO_LADO'            :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Humano/Lado.xml')
                                                                                }
                                                   ,'ANIMAL'                :   {
                                                                                    'GATO_FRENTE'           :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Animal/Gato_frente.xml')
                                                                                   ,'GATO_EXPANDIDA'        :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Rosto/Animal/Gato_expandida.xml')
                                                                                }
                                                   ,'CORPO'                 :   {
                                                                                    'CORPO'                 :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Corpo/Corpo.xml')
                                                                                   ,'CORPO_SUPERIOR'        :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Corpo/Corpo_alto.xml')
                                                                                   ,'CORPO_INFERIOR'        :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/haarcascades/Corpo/Corpo_baixo.xml')
                                                                                }
                                                }
    QUACK_TF                                =   {
                                                    'GERAL'                 :   {
                                                                                    'Diretorio'             :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/modelo_cortex')
                                                                                   ,'Modelo'                :   'cortex.pb'
                                                                                   ,'Descricao'             :   'cortex.pbtxt'
                                                                                }
                                                }
    # # --------------------------------------------------------------# #

    # Procedimento - Método de inicialização
    def __init__(self, p_configuracao):
        try:
            # Carrega a conexão ao DB para execuções
            # Para conexão com o SQL
            self.QUACK_CONFIG           =   p_configuracao
            # Carrega a conexão ao DB para execuções

            # Carrega as cores - METODO RANDOM PARA CARREGAMENTO DE CORES ALEATÓRIAS
            self.QUACK_COR              =   self.func_carrega_cores()
            # Carrega as cores - METODO RANDOM PARA CARREGAMENTO DE CORES ALEATÓRIAS

            # Carrega na memória os dados para reconhecimento
            #self.proc_carrega_face()
            self.proc_carrega_tf()
            # Carrega na memória os dados para reconhecimento

        except Exception  as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][INIT][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)

            self.quack_arquivo_log(vtmp_erro)
            sys.exit()
        except ValueError as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][INIT][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)
            sys.exit()
    # Procedimento - Método de inicialização

    # # --------------------------------------------------------------# #

    # Método de suporte QUACK - Salva o arquivo na base
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
    # Método de suporte QUACK - Salva o arquivo na base

    # # --------------------------------------------------------------# #    

    # Função - Carregamento de vetores para imagens - Carregamento de cores.
    def func_carrega_cores(self):
        # VARIÁVEIS - PROC_CARREGA_CORES
        v_cores     =   []
        # VARIÁVEIS - PROC_CARREGA_CORES

        # PROCEDIMENTO PARA CARREGAMENTO DE CORES ALEATÓRIAS
        for curreg in range(0,99):
            try:
                v_dicionario    =   {}

                # Obtém a cor RGB # ---> CARREGA DICIONÁRIO
                v_dicionario["VERMELHO"]    =   int(np.random.randint(0,255))
                v_dicionario["VERDE"]       =   int(np.random.randint(0,255))
                v_dicionario["AZUL"]        =   int(np.random.randint(0,255))
                # Obtém a cor RGB # ---> CARREGA DICIONÁRIO

                v_cores.append(v_dicionario)
            except Exception as p_erro:
                # Mais detalhes sobre o erro
                ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
                ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

                vtmp_erro   =   '[VISAO][FUNC_CARREGA_CORES][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
                self.quack_arquivo_log(vtmp_erro)
                sys.exit()
            except ValueError as p_erro:
                # Mais detalhes sobre o erro
                ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
                ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

                vtmp_erro   =   '[VISAO][FUNC_CARREGA_CORES][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
                self.quack_arquivo_log(vtmp_erro)
                sys.exit()
        # PROCEDIMENTO PARA CARREGAMENTO DE CORES ALEATÓRIAS

        # Finaliza e retorna a lista de cores
        return v_cores
        # Finaliza e retorna a lista de cores
    # Função - Carregamento de vetores para imagens - Carregamento de cores.

    # # --------------------------------------------------------------# #

    # Função para carregamento do tensorflow e suas características de treinamento
    def proc_carrega_tf(self):
        # Carrega os modelos TF para a memória
        # lOOP PARA COLETA DOS DADOS DA TUPLA
        for csr_modelo in self.QUACK_TF:
             # Inicializa o método tensorflow e carrega à memória #
            try:
                # Inicializa a variável
                v_tmp_modelo    =   {}

                # Marca as versões para de modelo, descrição e patchs
                # Carrega o modelo do tensorflow
                v_caminho_deteccao          =   os.path.join(self.QUACK_TF[csr_modelo]['Diretorio'], self.QUACK_TF[csr_modelo]['Modelo'])
                # Carrega a descrição do tensorflow
                v_caminho_descricao         =   os.path.join(self.QUACK_TF[csr_modelo]['Diretorio'], self.QUACK_TF[csr_modelo]['Descricao'])
                # Cria um mapa de descrições para o modelo tensorflow
                v_mapa_descricao            =   cx_desc.load_labelmap(v_caminho_descricao)
                # Transforma o mapa de descrições em categorias
                v_categoria                 =   cx_desc.convert_label_map_to_categories(v_mapa_descricao,max_num_classes=90,use_display_name=True)
                # Cria índices para a categoria criada
                v_indice_categoria          =   cx_desc.create_category_index(v_categoria)

                v_treino                        =   tf.Graph()                              ## Informa que um gráfico será carregado para o Tensorflow
                with v_treino.as_default():                                                 ## Marca os valores padrões o .PB carregado!
                    v_definicao                 =   tf.GraphDef()                           ## Inicia a definição de objetos reconhecidos do tensorflow e suas descrições
                    with tf.gfile.GFile(v_caminho_deteccao, 'rb') as fid:                   ## Nomeia os dados de detecção como f_id!
                        v_serializacao          =   fid.read()                              ## Realiza uma leitura de todos os ID's(Fids)
                        v_definicao.ParseFromString(v_serializacao)                         ## Cria uma serialização das classes geradas e seus dados -> MARCA TUDO PARA STRING
                        tf.import_graph_def(v_definicao, name='')                           ## Gera uma definição sem nomeclatura - À obter da lista pbtxt
                    ## Gera a sessão pertinente
                    v_sessao                    = tf.Session(graph=v_treino)       #        # Marca a detecção e procura por dados do usuário

            except Exception as p_erro:
                # Mais detalhes sobre o erro
                ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
                ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

                vtmp_erro   =   '[VISAO][PROC_CARREGA_TF][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
                self.quack_arquivo_log(vtmp_erro)
                v_tmp_modelo    =   {
                                        'SUCESSO'       :   False
                                       ,'MENSAGEM'      :   p_erro
                                       ,'MODELO'        :   None
                                       ,'DESCRICAO'     :   None
                                       ,'MAPA'          :   None
                                       ,'CATEGORIA'     :   None
                                       ,'INDICE'        :   None
                                       ,'TREINO'        :   None
                                       ,'DEFINICAO'     :   None
                                       ,'SERIE'         :   None
                                       ,'SESSAO'        :   None
                                    }
            except ValueError as p_erro:
                # Mais detalhes sobre o erro
                ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
                ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

                vtmp_erro   =   '[VISAO][PROC_CARREGA_TF][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
                self.quack_arquivo_log(vtmp_erro)
                v_tmp_modelo    =   {
                                        'SUCESSO'       :   False
                                       ,'MENSAGEM'      :   p_erro
                                       ,'MODELO'        :   None
                                       ,'DESCRICAO'     :   None
                                       ,'MAPA'          :   None
                                       ,'CATEGORIA'     :   None
                                       ,'INDICE'        :   None
                                       ,'TREINO'        :   None
                                       ,'DEFINICAO'     :   None
                                       ,'SERIE'         :   None
                                       ,'SESSAO'        :   None
                                    }
            else:
                v_tmp_modelo    =   {
                                        'SUCESSO'       :   True
                                       ,'MENSAGEM'      :   ''
                                       ,'MODELO'        :   v_caminho_deteccao
                                       ,'DESCRICAO'     :   v_caminho_descricao
                                       ,'MAPA'          :   v_mapa_descricao
                                       ,'CATEGORIA'     :   v_categoria
                                       ,'INDICE'        :   v_indice_categoria
                                       ,'TREINO'        :   v_treino
                                       ,'DEFINICAO'     :   v_definicao
                                       ,'SERIE'         :   v_serializacao
                                       ,'SESSAO'        :   v_sessao
                                    }
            finally:
                self.QUACK_MODELO_TF.append(v_tmp_modelo)
        # Carrega os modelos TF para a memória
    # Função para carregamento do tensorflow e suas características de treinamento

    # # --------------------------------------------------------------# #

    # Carregamento via câmera ou URL
    def executa(self, p_configuracao):
        try:
            # Armazena a configuração atual com as lista atualizadas
            self.QUACK_CONFIG   =   p_configuracao
            # Armazena a configuração atual com as lista atualizadas

            # Armazena os dados das câmeras para primeira composição das imagens, os dados serão obtidos
            # através de uma lista pré-cadastrada ou quiçá da webcam, de acordo com o modelo de negócio aplicado.
            # Cria a piscina de requisições - PARALELISMO APLICADO THREADING
            vmulti_piscina      =   [Thread(target=self.visao,args=(self.QUACK_CONFIG['Lista']['Camera'][curreg][1],self.QUACK_CONFIG['Lista']['Camera'][curreg][0], self.QUACK_CONFIG['Lista']['Camera'][curreg][3], self.QUACK_CONFIG['Lista']['Camera'][curreg][2])) for curreg in range(len(self.QUACK_CONFIG['Lista']['Camera']))]
            # Cria a piscina de requisições - PARALELISMO APLICADO THREADING

            # Prepara o pool para execução - Processo
            for vpool_exec in vmulti_piscina:
                vpool_exec.start()
            # Prepara o pool para execução - Processo

        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][EXECUTAR][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)
            sys.exit()
    # Carregamento via câmera ou URL

    # # --------------------------------------------------------------# #

    # A visão em seu estado inicial - Coleta das imagens para tratamento e composição
    def visao(self, p_texto, p_caminho, p_ponto_corte, p_id_sistema_camera):
        try:
            vtmp_erro       =   '[Inicializada][' + p_texto + '] - ' + p_caminho
            self.quack_arquivo_log(vtmp_erro)
            # Prepara o loop para execução da visao
            while True:
                try:
                    # Inicializa a captura marcando o alvo/caminho que será atingido
                    vmb_visao_captura    =   cv2.VideoCapture(p_caminho)
                    # Inicializa a captura marcando o alvo/caminho que será atingido

                    ## Coleta as câmeras e seus dados
                    vmb_ret, vmb_camera                     =   vmb_visao_captura.read()
                    #vmb_camera                  =   cv2.flip(vmb_camera,1)
                    vmb_reconhecimento, vtmp_img_tratada    =   self.func_inicia_rec(vmb_camera, p_texto, p_ponto_corte, p_id_sistema_camera)

                    if not vmb_reconhecimento:
                        vtmp_erro       =   '[PARADA DETECTADA] - Tentando reconexão com ' + p_texto
                        self.quack_arquivo_log(vtmp_erro)
                    else:
                        # Escreve a imagem para visualização
                        if self.QUACK_CONFIG['Quack']['Exibicao']:
                            cv2.imshow(p_texto, vtmp_img_tratada)
                        # Executa o prometeus para detecção

                    ## Monitora as teclas usadas, se clicado "Q" ...
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        # Encerra o loop
                        break

                    ## Encerra a coleta de imagens da câmera
                    vmb_visao_captura.release()
                except Exception as e:
                    break

            ## Ao sair do loop a janela criada ficava em aberto ... necessário destruí-la.
            cv2.destroyAllWindows()
            # Prepara o loop para execução da visao
        except Exception as p_erro:
            ## Encerra a coleta de imagens da câmera
            vmb_visao_captura.release()

            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)
            sys.exit()
    # A visão em seu estado inicial - Coleta das imagens para tratamento e composição

    # # --------------------------------------------------------------# #

    # Treinamento - Inicia o reconhecimento de características macro
    def func_inicia_rec(self, p_imagem, p_texto, p_corte, p_id_sistema_camera):
        try:
            if p_imagem is None:
                vtmp_erro       =   '[Alerta] - Nenhuma imagem obtida para [' + p_texto +'] - Parada eminente.'
                self.quack_arquivo_log(vtmp_erro)
                return False;

            v_imagem            =   p_imagem.copy()
            v_imagem_retorno    =   p_imagem.copy()
            v_imagem_array      =   Imagem.fromarray(v_imagem)
            v_altura, v_largura =   v_imagem_array.size
            v_indice_cor        =   0

            # Com a imagem em mãos ... inicia tratamento
            # Percorrerá o modelo de detecção em busca dos objetos
            for csr_aprendizado in self.QUACK_MODELO_TF:
                if csr_aprendizado['SUCESSO']:
                    # Expande a imagem para o seguinte formato: [1, None, None, 3]
                    # Em resumo, deixa a imagem 3x maior para deteção
                    v_imagem_expandida  =   np.expand_dims(v_imagem, axis=0)
                    # Expande a imagem para o seguinte formato: [1, None, None, 3]

                    # Inicializa o método de deteção do Tensorflow
                    # Informa ao Tensorflow que se trata de uma imagem
                    v_imagem_tf         =   csr_aprendizado['TREINO'].get_tensor_by_name('image_tensor:0')

                    # Inicia a preparação das áreas onde a detecção ocorreu
                    v_dimensoes         =   csr_aprendizado['TREINO'].get_tensor_by_name('detection_boxes:0')

                    # Marca a pontuação de semelhança entre o objeto detectado e o padrão esperado
                    v_pontos_tf         =   csr_aprendizado['TREINO'].get_tensor_by_name('detection_scores:0')

                    # Marca também o método necessário para a escolha da classe correta
                    v_classe            =   csr_aprendizado['TREINO'].get_tensor_by_name('detection_classes:0')

                    # Marca o local de retorno para o tensorflow informando as detecções
                    v_deteccoes         =   csr_aprendizado['TREINO'].get_tensor_by_name('num_detections:0')

                    # Executa a detecção via tensorflow (RUN)
                    (csr_dimensoes, csr_pontuacao, csr_classe, csr_qtde_deteccao) = csr_aprendizado['SESSAO'].run([v_dimensoes, v_pontos_tf, v_classe, v_deteccoes],feed_dict={v_imagem_tf: v_imagem_expandida})
                    # Percorrerá cada modelo da detecção atrás de informações

                    #v_qtde_encontrada = sum([1 for csr_iterador in range(0,len(np.squeeze(csr_dimensoes))) if ((np.squeeze(csr_pontuacao)[csr_iterador]) *100) >= p_corte])

                    #print('[',p_texto,'] - Detectados [', v_qtde_encontrada,']')

                    # Coleta as informações obtidas - Somente as que geraram dimensões
                    for csr_iterador in range(0,len(np.squeeze(csr_dimensoes))):
                        # Apenas registros dentro dos padrões informados serão tratados
                        if ((np.squeeze(csr_pontuacao)[csr_iterador]) *100) >= p_corte:
                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]
                            # (left, right, top, bottom)
                            vmb_dim_sup_dir     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(1) * int(v_altura))    #  * v_altura
                            vmb_dim_sup_esq     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(3) * int(v_altura))
                            vmb_dim_inf_dir     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(2)* int(v_largura))    # * v_largura
                            vmb_dim_inf_esq     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(0) * int(v_largura))
                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]

                            # Delimita a área de observação do dado detectado
                            vmbtmp_dimensoes    =   (vmb_dim_sup_dir, vmb_dim_sup_esq, vmb_dim_inf_dir, vmb_dim_inf_esq)
                            vtmp_imagem         =   v_imagem[vmb_dim_inf_esq:vmb_dim_inf_dir, vmb_dim_sup_dir:vmb_dim_sup_esq]
                            # Delimita a área de observação do dado detectado

                            # Carega o log para o banco de dados.
                            self.proc_salva_log(v_imagem,vtmp_imagem, p_id_sistema_camera, csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['id'], vmb_dim_sup_dir, vmb_dim_sup_esq, vmb_dim_inf_dir, vmb_dim_inf_esq, ((np.squeeze(csr_pontuacao)[csr_iterador]) *100))
                            # Carega o log para o banco de dados.

                            # Desenha a área numa cópia para retorno
                            cv2.rectangle(v_imagem_retorno, (vmb_dim_sup_dir, vmb_dim_inf_dir), (vmb_dim_sup_esq, vmb_dim_inf_esq), (self.QUACK_COR[v_indice_cor]["VERMELHO"], self.QUACK_COR[v_indice_cor]["AZUL"], self.QUACK_COR[v_indice_cor]["VERDE"]), 1)
                            vtmp_texto_imagem   =   str(csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize()) + ": " + str(((np.squeeze(csr_pontuacao)[csr_iterador]) *100)) + "%"
                            cv2.putText(v_imagem_retorno, vtmp_texto_imagem, (vmb_dim_sup_dir+20, vmb_dim_inf_dir+20), self.QUACK_FONTE, 1, (self.QUACK_COR[v_indice_cor]["VERMELHO"], self.QUACK_COR[v_indice_cor]["AZUL"], self.QUACK_COR[v_indice_cor]["VERDE"]), 2, cv2.LINE_AA)
                            # Desenha a área numa cópia para retorno

                            # Marca a tupla de elemento identificado
                            #v_tmp_imagem_corte          =   self.func_imagem_para_base64(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo])
                            #v_tmp_imagem_array          =   Imagem.fromarray(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo])
                            #v_tmp_altura, v_tmp_largura =   v_tmp_imagem_array.size

                            # Cria os dados do elemento identificado e suas respectivas pontuações
                            #v_tmp_ret_elemento  =   {
                            #                            'elemento'  :   csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize()
                            #                           ,'pontuacao' :   ((np.squeeze(csr_pontuacao)[csr_iterador]) * 100)
                            #                        }
                            # Adiciona o dado da identificação na array
                            #if csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize() not in v_indicador_dict['descricao']:
                            #    v_indicador_dict['descricao'].append(csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize())
                            #    v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                            # Cria os dados do elemento identificado e suas respectivas pontuações
                            # Marca a tupla de elemento identificado

                            '''
                            # Inicia detecção facial na imagem
                            for csr_deteccao_modelo in self.VMBRAUNA_MODELO_FACIAL:
                                # Verifica se houve sucesso no carregador do reconhecimento facial
                                if csr_deteccao_modelo['SUCESSO']:
                                    # Array para imagens escolhidas - Detectará a quantidade de rostos
                                    v_dimensao_reconhecida  =   csr_deteccao_modelo['METODO'].detectMultiScale(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo], scaleFactor=1.2, minNeighbors=(int(int(p_corte)/10)))

                                    # Verifica se ocorreu alguma detecção e prepara para marcação
                                    if len(v_dimensao_reconhecida) > 0:
                                        # Loop para dados encontrados
                                        for (csr_alto, csr_direita, csr_baixo, csr_esquerda) in v_dimensao_reconhecida:
                                            # Trata cada uma das coordenadas para retorno
                                            v_face_alto         =   csr_alto
                                            v_face_baixo        =   csr_alto    +   csr_baixo
                                            v_face_direita      =   csr_direita
                                            v_face_esquerda     =   csr_direita +   csr_esquerda
                                            # Trata cada uma das coordenadas para retorno

                                            # Desenha o objeto encontrado
                                            cv2.rectangle(v_imagem_retorno, (v_alto, v_direita), (v_baixo, v_esquerda), (self.VCX_CORES[v_indice_cor]["VERMELHO"], self.VCX_CORES[v_indice_cor]["AZUL"], self.VCX_CORES[v_indice_cor]["VERDE"]), 1)
                                            # Desenha o objeto encontrado

                                            # Preparação para inserir a descrição
                                            # Verifica se o termo que será inserido já não foi detectado anteriormente
                                            # Adiciona o tipo
                                            #if csr_deteccao_modelo['TIPO'].capitalize() not in v_indicador_dict['descricao']:
                                            #    # Cria os dados do elemento identificado e suas respectivas pontuações
                                            #    v_tmp_ret_elemento  =   {
                                            #                                'elemento'  :   csr_deteccao_modelo['TIPO'].capitalize()
                                            #                               ,'pontuacao' :   p_json['corte']
                                            #                            }
                                            #    # Adiciona o dado da identificação na array
                                            #    v_indicador_dict['descricao'].append(csr_deteccao_modelo['TIPO'].capitalize())
                                            #    v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                                            #    # Cria os dados do elemento identificado e suas respectivas pontuações
                                            # Adiciona o subtipo
                                            #if csr_deteccao_modelo['SUBTIPO'].capitalize() not in v_indicador_dict['descricao']:
                                            #    # Cria os dados do elemento identificado e suas respectivas pontuações
                                            #    v_tmp_ret_elemento  =   {
                                            #                                'elemento'  :   csr_deteccao_modelo['SUBTIPO'].capitalize()
                                            #                               ,'pontuacao' :   p_json['corte']
                                            #                            }
                                            #    # Adiciona o dado da identificação na array
                                            #    v_indicador_dict['descricao'].append(csr_deteccao_modelo['SUBTIPO'].capitalize())
                                            #    v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                                            #    # Cria os dados do elemento identificado e suas respectivas pontuações
                            # Inicia detecção facial na imagem
                            '''

                            # Incrementa o contador de cores
                            v_indice_cor += 1       # Incrementa o índice de cores
                            if v_indice_cor > 99:   # Se o índice for superior à 99
                                v_indice_cor = 0    # Retorna ao registro inicial
                            # Incrementa o contador de cores
                        # Apenas registros dentro dos padrões informados serão tratados
            # Percorrerá o modelo de detecção em busca dos objetos

            return True, v_imagem_retorno
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][FUNC_INICIA_REC][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro) + ' | -- | ' + str(ecx_tipo) + ' | -- | ' + str(ecx_dados)  + ' | -- | ' + str(ecx_nome)
            self.quack_arquivo_log(vtmp_erro)

            return False, v_imagem_retorno
    # Treinamento - Inicia o reconhecimento de características macro

    # # --------------------------------------------------------------# #    

    # Função para validação da imagem em base64 informada
    def func_valida_base64(self,p_base64):
        try:
            v_imagem    =   self.func_base64_para_imagem(p_base64)
            v_altura, v_largura, v_canal = v_imagem.shape

            return (v_altura is not None and v_largura is not None and v_altura > 0 and v_largura > 0)
        except Exception  as p_erro:
            return False
        except ValueError as p_erro:
            return False
    # Função para validação da imagem em base64 informada

    # # --------------------------------------------------------------# #    

    # Função - Converte base64 para imagem
    def func_base64_para_imagem(self,p_base64):
        try:
            v_imagem_bytes  =   imread(io.BytesIO(base64.b64decode(p_base64)))
            v_imagem_final  =   cv2.cvtColor(v_imagem_bytes, cv2.COLOR_RGB2BGR)

            return v_imagem_final
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][FUNC_BASE64_PARA_IMAGEM][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.quack_arquivo_log(vtmp_erro)
            return None
    # Função - Converte base64 para imagem

    # # --------------------------------------------------------------# #    

    # Função - Converte Imagem para base64
    def func_imagem_para_base64(self,p_imagem):
        try:
            v_dimensao, v_imagem    =   cv2.imencode('.jpg', p_imagem)
            v_img_bytes             =   base64.b64encode(v_imagem)
            v_img_string            =   v_img_bytes.decode()

            return v_img_string
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][FUNC_IMAGEM_PARA_BASE64][ERRO][' + ecx_dados.tb_lineno + '] - ' + p_erro
            self.proc_salva_arquivo(vtmp_erro)
            return None
    # Função - Converte Imagem para base64

    # # --------------------------------------------------------------# #    

    # Função para transformar dimensões DLIB em OPENCV
    def func_dimensao_dlib_opencv(p_dimensao):
        try:
            return rect.top(), rect.right(), rect.bottom(), rect.left()
        except Exception as e:
            return None, None, None, None
    # Função para transformar dimensões DLIB em OPENCV

    # # --------------------------------------------------------------# #    

    # Função para transformar dimensões OpenCV em DLib
    def func_dimensao_opencv_dlib(p_dimensao):
        try:
            return dlib.rectangle(css[3], css[0], css[1], css[2])
        except Exception as e:
            return None
    # Função para transformar dimensões OpenCV em DLib

    # # --------------------------------------------------------------# #    

    # Função para cortar as dimensões localizadas que estiverem excedendo a função inicial
    def func_aparar_dimensao(p_dimensao, p_img_original_dimensao):
        try:
            return max(p_dimensao[0], 0), min(p_dimensao[1], p_img_original_dimensao[1]), min(p_dimensao[2], p_img_original_dimensao[0]), max(p_dimensao[3], 0)
        except Exception as e:
            return None
    # Função para cortar as dimensões localizadas que estiverem excedendo a função inicial

    # # --------------------------------------------------------------# #    

    # Função para detectar rostos com base em distância euclidiana faces similares
    def func_euclidiana_rostos(p_rosto, p_rosto_comparar):
        # Optei por distância euclidiana por oferecer uma comparação boa, com um cálculo simples
        # caso a necessidade de executá-lo numa lista encadeada de tamanho gigantesca.
        
        # Até então nunca testado ... provavelmente necessitará ajustes

        # A distância euclidiana entre dois pontos é composta pela soma de todos os elementos ao quadrado
        # Subtraindo pela soma de todos os elementos de comparação ao quadrado
        # Pela raiz quadrada do resultado desta operação.

        # # # # # # # # # # # # # # # # # # # # # # # # # #
        # sqrt{(p_1-q_1)^2 + (p_2-q_2)^2+...+(p_n-q_n)^2} #
        # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Ou podemos usar a função da bib. matemática de  #
        # numpy chamada linalg.norm.                      #
        # # # # # # # # # # # # # # # # # # # # # # # # # #

        try:
            if len(p_rosto) == 0:
                return np.empty((0))

            return np.linalg.norm(p_rosto - p_rosto_comparar,axis=1)
        except Exception  as p_erro:
            return np.empty((0))
        except ValueError as p_erro:
            return np.empty((0))
    # Função para detectar rostos com base em distância euclidiana faces similare

    # # --------------------------------------------------------------# #    

    # Carrega uma imagem de um arquivo para array numpy
    def func_carrega_imagem(p_arquivo, p_modo='RGB'):
        try:
            v_imagem        =   Imagem.open(p_arquivo)

            if p_modo:
                v_imagem    =   v_imagem.convert(p_modo)

            return np.array(v_imagem)
        except Exception as p_erro:
            return None
        except ValueError as p_erro:
            return None
    # Carrega uma imagem de um arquivo para array numpy

    # # --------------------------------------------------------------# #    

    # Função - Transforma array em Imagem
    def func_img_expandida_para_normal(self, p_imagem_expandida):
        try:
            return np.squeeze(p_array_imagem, axis=0)
        except Exception as e:
            return None
    # Função - Transforma array em Imagem

    # # --------------------------------------------------------------# #    

    # Função para converter imagem numpy em imagem OpenCV
    def func_imagem_numpy_para_opencv(p_imagem):
        try:
            return np.zeros(p_imagem, np.unit8)
        except Exception as p_erro:
            return None
        except Exception as p_erro:
            return None
    # Função para converter imagem numpy em imagem OpenCV

    # # --------------------------------------------------------------# #    

    # Função para converter imagem opencv em imagem numpy
    def func_imagem_opencv_para_numpy(p_imagem):
        try:
            return np.asarray(p_imagem, dtype='uint8')
        except Exception as p_erro:
            return None
        except Exception as p_erro:
            return None
    # Função para converter imagem opencv em imagem numpy

    # # --------------------------------------------------------------# #    

    # Procedimento para armazenar no banco de dados todos os dados obtidos na detecção
    def proc_salva_log(self, p_imagem, p_imagem_cortada, p_id_lista_camera, p_id_classe, p_dim_sup_dir, p_dim_sup_esq, p_dim_inf_dir, p_dim_inf_esq, p_probabilidade):
        try:
            # Imagem para base64
            vtmp_imagem                 =   self.func_imagem_para_base64(p_imagem)
            if vtmp_imagem is None:
                vtmp_imagem             =   'null'
            # Imagem para base64

            # Imagem para base64
            vtmp_imagem_cortada         =   self.func_imagem_para_base64(p_imagem_cortada)
            if vtmp_imagem_cortada is None:
                vtmp_imagem_cortada     =   'null'
            # Imagem para base64            

            # Salva o novo registro
            vtmp_comando    =   'insert into camera_deteccao(id_lista_camera, id_elemento, probabilidade, dimensao_sup_esq, dimensao_sup_dir, dimensao_inf_esq, dimensao_inf_dir,base64, base64_elemento) values (' + str(p_id_lista_camera) + ','+str(p_id_classe)+ ','+str(p_probabilidade)+ ','+str(p_dim_sup_esq)+ ','+str(p_dim_inf_esq)+ ','+str(p_dim_sup_dir)+ ','+str(p_dim_inf_dir)+ ',%s,%s)'
            vtmp_dml        =   self.QUACK_CONFIG['Quack']['DB'].salva_log_arquivo(self.QUACK_CONFIG,vtmp_comando, vtmp_imagem, vtmp_imagem_cortada)
            # Salva o novo registro
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]

            vtmp_erro   =   '[VISAO][PROC_SALVA_LOG][ERRO][' + str(ecx_dados.tb_lineno) + '] - ' + str(p_erro)
            self.quack_arquivo_log(vtmp_erro)