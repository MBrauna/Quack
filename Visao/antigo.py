'''
Autor: Michel Brauna                                          Data: 17/01/2014


    ███╗   ███╗██████╗ ██████╗  █████╗ ██╗   ██╗███╗   ██╗ █████╗ 
    ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗  ██║██╔══██╗
    ██╔████╔██║██████╔╝██████╔╝███████║██║   ██║██╔██╗ ██║███████║
    ██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║██║   ██║██║╚██╗██║██╔══██║
    ██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
'''

## Bibliotecas externas para reconhecimento facial
import  argparse                                                                                ## Biblioteca para tratamento de argumentos de entrada
import  base64                                                                                  ## Biblioteca para tratamento em base64
import  cv2                                                                                     ## Biblioteca para reconhecimento facial
import  dlib                                                                                    ## Biblioteca para comparação de imagens - C++
import  io                                                                                      ## Biblioteca para escrita em diversos formatos
import  json                                                                                    ## Biblioteca para manipulação de dados via JSON
import  numpy                           as np                                                   ## Biblioteca para cálculos matemáticos
import  os                                                                                      ## Biblioteca para acesso à informações do sistema operacional
import  pyscopg2                                                                                ## Biblioteca para consulta no banco de dados
import  sys                                                                                     ## Biblioteca para controle de tempo de execução e retorno dos dados
import  tensorflow                      as tf                                                   ## Biblioteca para aprendizagem de máquina
import  time                                                                                    ## Biblioteca para obtenção e cálculo de tempo

import  PIL.Image                       as Imagem                                               ## Biblioteca para tratamento de imagens
import  PIL.ImageColor                  as Imagem_Cor                                           ## Biblioteca para tratamento de cores de imagens
import  PIL.ImageDraw                   as Imagem_Escreve                                       ## Biblioteca para escrita de imagens
import  PIL.ImageFont                   as Imagem_Fonte                                         ## Biblioteca para fonte das escritas

from    multiprocessing                 import  Queue ,Pool                                     ## Biblioteca para filas de processamentos
from    object_detection.utils          import  label_map_util      as cx_desc                  ## Biblioteca para geração do texto nas imagens
from    object_detection.utils          import  visualization_utils as visualizacao             ## Biblioteca para visualização dos textos
from    datetime                        import  date                                            ## Biblioteca para trabalho com tempo
from    imageio                         import imread                                           ## Biblioteca para leitura e escrita de imagens em N formatos
## Bibliotecas externas para reconhecimento facial 





class mbrauna_visao:


    # # --------------------------------------------------------------# #
    # #                    VARIAVEL INTERNA - ARRAY                   # #
    # # --------------------------------------------------------------# #
    VMBRAUNA_COR                            =   []
    VMBRAUNA_MODELO_TF                      =   []
    VMBRAUNA_MODELO_FACIAL                  =   []
    VMBRAUNA_CONEXAO                        =   None

    # # --------------------------------------------------------------# #
    VMBRAUNA_EXTENSAO                       =   [
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
    VMBRAUNA_FACIAL                         =   {
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
    # # --------------------------------------------------------------# #
    VMBRAUNA_TF                             =   {
                                                    'GERAL'                 :   {
                                                                                    'Diretorio'             :   os.path.join(os.path.dirname(os.path.abspath(__file__)),r'Deteccao/Biblioteca/modelo_cortex')
                                                                                   ,'Modelo'                :   'cortex.pb'
                                                                                   ,'Descricao'             :   'cortex.pbtxt'
                                                                                }
                                                }
    # # --------------------------------------------------------------# #




    # Procedimento - Método de inicialização
    def __init__(self):
        try:
            # Carrega as cores - METODO RANDOM PARA CARREGAMENTO DE CORES ALEATÓRIAS
            self.VMBRAUNA_COR  =   self.func_carrega_cores()
            # Carrega as cores - METODO RANDOM PARA CARREGAMENTO DE CORES ALEATÓRIAS

            # Carrega na memória os dados para reconhecimento
            self.proc_carrega_face()
            self.proc_carrega_tf()
            # Carrega na memória os dados para reconhecimento

            # Inicializa a conexão ao banco de dados
            self.VMBRAUNA_CONEXAO  =   psycopg2.connect("dbname='Saturno' user='Saturno' host='localhost' password='ABC123abc.'")
            # Inicializa a conexão ao banco de dados
        except Exception  as p_erro:
            print('Procedimento finalizado! Não foi possível inicializar o sistema MBRAUNA')
            print('MBRAUNAERROR-0001 - ',p_erro)
            sys.exit()
        except ValueError as p_erro:
            print('Procedimento finalizado! Não foi possível inicializar o sistema MBRAUNA')
            print('MBRAUNAERROR-0002 - ',p_erro)
            sys.exit()
    # Procedimento - Método de inicialização

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

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
                print('[PROC_CARREGA_CORES|ERRO|EXCEPTION] : ',p_erro)
            except ValueError as p_erro:
                print('[PROC_CARREGA_CORES|ERRO|VALUEERROR] : ',p_erro)
            
        # PROCEDIMENTO PARA CARREGAMENTO DE CORES ALEATÓRIAS

        # Finaliza e retorna a lista de cores
        return v_cores
        # Finaliza e retorna a lista de cores
    # Função - Carregamento de vetores para imagens - Carregamento de cores.

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    
    # Procedimento - Carregamento de modelo tensorflow
    def proc_carrega_tf(self):
        # Carrega os modelos TF para a memória
        # lOOP PARA COLETA DOS DADOS DA TUPLA
        for csr_modelo in self.VMBRAUNA_TF:
             # Inicializa o método tensorflow e carrega à memória #
            try:
                # Inicializa a variável
                v_tmp_modelo    =   {}

                # Marca as versões para de modelo, descrição e patchs
                # Carrega o modelo do tensorflow
                v_caminho_deteccao          =   os.path.join(self.VMBRAUNA_TF[csr_modelo]['Diretorio'], self.VMBRAUNA_TF[csr_modelo]['Modelo'])
                # Carrega a descrição do tensorflow
                v_caminho_descricao         =   os.path.join(self.VMBRAUNA_TF[csr_modelo]['Diretorio'], self.VMBRAUNA_TF[csr_modelo]['Descricao'])
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
                print('[ERRO] - Ocorreu um problema na detecção[1]:',p_erro)
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
                print('[ERRO] - Ocorreu um problema na detecção[2]:',p_erro)
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
                self.VMBRAUNA_MODELO_TF.append(v_tmp_modelo)
        # Carrega os modelos TF para a memória
    # Procedimento - Carregamento de modelo tensorflow

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Procedimento - Carregamento de modelo de faces
    def proc_carrega_face(self):
        for csr_modelo in self.VMBRAUNA_FACIAL:
            for csr_sub_modelo in self.VMBRAUNA_FACIAL[csr_modelo]:
                try:
                    v_tmp_modelo    =   {}
                    v_deteccao      =   cv2.CascadeClassifier(self.VMBRAUNA_FACIAL[csr_modelo][csr_sub_modelo])
                except Exception  as p_erro:
                    # Modelo de detecção apresentou erros logo, necessário marcá-lo
                    v_tmp_modelo    =   {
                                            'SUCESSO'   :   False
                                           ,'METODO'    :   None
                                           ,'TIPO'      :   csr_modelo
                                           ,'SUBTIPO'   :   csr_sub_modelo
                                        }
                    # Modelo de detecção apresentou erros logo, necessário marcá-lo
                except ValueError as p_erro:
                    # Modelo de detecção apresentou erros logo, necessário marcá-lo
                    v_tmp_modelo    =   {
                                            'SUCESSO'   :   False
                                           ,'METODO'    :   None
                                           ,'TIPO'      :   csr_modelo
                                           ,'SUBTIPO'   :   csr_sub_modelo
                                        }
                    # Modelo de detecção apresentou erros logo, necessário marcá-lo
                else:
                    # Se tudo ocorreu de forma correta ... marca o sucesso e o método
                    v_tmp_modelo    =   {
                                            'SUCESSO'   :   True
                                           ,'METODO'    :   v_deteccao
                                           ,'TIPO'      :   csr_modelo
                                           ,'SUBTIPO'   :   csr_sub_modelo
                                        }
                    # Se tudo ocorreu de forma correta ... marca o sucesso e o método
                finally:
                    self.VMBRAUNA_MODELO_FACIAL.append(v_tmp_modelo)
    # Procedimento - Carregamento de modelo de faces

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para execução e reconhecimento de estruturas e faces
    def func_inicia_rec(self, p_imagem):
        try:
            v_corte             =   70

            v_imagem            =   p_imagem.copy()
            v_imagem_retorno    =   v_imagem.copy()
            v_imagem_array      =   Imagem.fromarray(v_imagem)
            v_altura, v_largura =   v_imagem_array.size

            # Com a imagem em mãos ... inicia tratamento
            # Percorrerá o modelo de detecção em busca dos objetos
            for csr_aprendizado in self.VMBRAUNA_MODELO_TF:
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

                    # Coleta as informações obtidas - Somente as que geraram dimensões
                    for csr_iterador in range(0,len(np.squeeze(csr_dimensoes))):
                        # Apenas registros dentro dos padrões informados serão tratados
                        if ((np.squeeze(csr_pontuacao)[csr_iterador]) *100) >= v_corte:

                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]
                            # (left, right, top, bottom)
                            vcx_alto        =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(1) * int(v_altura))    #  * v_altura
                            vcx_baixo       =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(3) * int(v_altura))
                            vcx_direita     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(2)* int(v_largura))    # * v_largura
                            vcx_esquerda    =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(0) * int(v_largura))
                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]

                            # Desenha a área numa cópia para retorno
                            cv2.rectangle(v_imagem_retorno, (vcx_alto, vcx_direita), (vcx_baixo, vcx_esquerda), (self.VMBRAUNA_COR[v_indice_cor]["VERMELHO"], self.VMBRAUNA_COR[v_indice_cor]["AZUL"], self.VMBRAUNA_COR[v_indice_cor]["VERDE"]), 1)
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
                            print(csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize())


                            # Inicia detecção facial na imagem
                            for csr_deteccao_modelo in self.VMBRAUNA_MODELO_FACIAL:
                                # Verifica se houve sucesso no carregador do reconhecimento facial
                                if csr_deteccao_modelo['SUCESSO']:
                                    # Array para imagens escolhidas - Detectará a quantidade de rostos
                                    v_dimensao_reconhecida  =   csr_deteccao_modelo['METODO'].detectMultiScale(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo], scaleFactor=1.2, minNeighbors=(int(int(v_corte)/10)))

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

                            # Incrementa o contador de cores
                            v_indice_cor += 1       # Incrementa o índice de cores
                            if v_indice_cor > 99:   # Se o índice for superior à 99
                                v_indice_cor = 0    # Retorna ao registro inicial
                            # Incrementa o contador de cores
                        # Apenas registros dentro dos padrões informados serão tratados
            # Percorrerá o modelo de detecção em busca dos objetos
        except Exception as e:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            print(ecx_nome)
        finally:
            return v_imagem_retorno
        
    # Função para execução e reconhecimento de estruturas e faces

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para reconhecimento de estruturas e faces
    def func_exec(self, p_json):
        # DECLARAÇÃO DE VARIÁVEIS
        v_indice_cor        =   0
        v_indicadores       =   {
                                    'original'  :   {
                                                        'base64'        :   None
                                                       ,'dimensao'      :   {
                                                                                'altura'    :   None
                                                                               ,'largura'   :   None
                                                                            }
                                                    }
                                   ,'final'     :   {
                                                        'base64'        :   None
                                                       ,'dimensao'      :   {
                                                                                'altura'    :   None
                                                                               ,'largura'   :   None
                                                                            }
                                                    }
                                   ,'lista'     :   []
                                }
        v_indicador_dict    =   {
                                    'base64'    :   None
                                   ,'dimensao'  :   {
                                                        'altura'    :   None
                                                       ,'largura'   :   None

                                                    }
                                   ,'limite'    :   {
                                                        'x1'    :   None
                                                       ,'x2'    :   None
                                                       ,'y1'    :   None
                                                       ,'y2'    :   None
                                                    }
                                   ,'cor'       :   {
                                                        'Vermelho'      :   None
                                                       ,'Verde'         :   None
                                                       ,'Azul'          :   None
                                                    }
                                   ,'elemento'  :   []
                                   ,'descricao' :   []
                                }
        # DECLARAÇÃO DE VARIÁVEIS

        try:
            # Verifica se um JSON foi realmente recebido.
            # TODO JSON É UM DICT
            if type(p_json) is not dict:
                raise ValueError('Os parâmetros não foram satisfeitos, é esperado um JSON, foi recebido um ' + str(type(p_json)) + '! Verifique.')
            # Verifica se um JSON foi realmente recebido.


            # Verifica se todas as informações necessárias foram preenchidas
            # Verificação para usuário
            if 'usuario' not in p_json:
                raise ValueError('[USUARIO] não identificado! Verifique documentação.')
            elif type(p_json['usuario']) is not int:
                raise ValueError('O elemento [USUARIO] está fora do padrão! Verifique documentação.')
            # Verificação para TOKEN
            elif 'token' not in p_json:
                raise ValueError('[TOKEN] não identificado! Verifique a documentação.')
            elif type(p_json['token']) is not str:
                raise ValueError('O elemento [TOKEN] está fora do padrão! Verifique documentação.')
            # Verificação para CORTE
            elif 'corte' not in p_json:
                raise ValueError('[CORTE] não identificado! Verifique a documentação.')
            elif type(p_json['corte']) is not int:
                raise ValueError('O elemento [CORTE] está fora do padrão! Verifique documentação.')
            elif p_json['corte'] not in range(0,101):
                raise ValueError('O ponto de corte está fora do padrão [0:100]! Verifique a docuemntação.')
            # Verificação para IMAGEM
            elif 'imagem' not in p_json:
                raise ValueError('[IMAGEM] Não identificada! Verifique a documentação.')
            elif type(p_json['imagem']) is not dict:
                raise ValueError('O elemento [IMAGEM] está fora do padrão! Verifique documentação.')
            # Verificação para base64
            elif 'base64' not in p_json['imagem']:
                raise ValueError('[BASE64] não identificada! Verifique a docuemntação.')
            elif type(p_json['imagem']['base64']) is not str:
                raise ValueError('O elemento [BASE64] está fora do padrão! Verifique documentação.' + p_json['imagem']['base64'])
            elif not self.func_valida_base64(p_json['imagem']['base64']):
                raise ValueError('O elemento [BASE64] não é uma imagem válida! Verifique documentação.')
            # Verificação para Dimensão
            elif 'dimensao' not in p_json['imagem']:
                raise ValueError('[DIMENSAO] não identificada! Verifique a documentação.')
            elif type(p_json['imagem']['dimensao']) is not dict:
                raise ValueError('O elemento [DIMENSAO] está fora do padrão! Verifique documentação.')
            # Verificação para Altura
            elif 'altura' not in p_json['imagem']['dimensao']:
                raise ValueError('[ALTURA] não identificada! Verifique a documentação.')
            elif type(p_json['imagem']['dimensao']['altura']) is not int:
                raise ValueError('O elemento [altura] está fora do padrão! Verifique documentação.')
            # Verificação para largura
            elif 'largura' not in p_json['imagem']['dimensao']:
                raise ValueError('[LARGURA] não identificada! Verifique a documentação.')
            elif type(p_json['imagem']['dimensao']['largura']) is not int:
                raise ValueError('O elemento [LARGURA] está fora do padrão! Verifique documentação.')
            # Verifica se todas as informações necessárias foram preenchidas

            # - Transformação de dados - pontuação e imagem
            v_imagem            =   self.func_base64_para_imagem(p_json['imagem']['base64'])
            v_imagem_retorno    =   v_imagem.copy()
            v_imagem_array      =   Imagem.fromarray(v_imagem)
            v_altura, v_largura =   v_imagem_array.size
            # - Transformação de dados - pontuação e imagem

            # Inicia a construção do JSON de indicadores
            # Monta os dados da dimensão inicial
            v_indicadores['original']['base64']                 =   p_json['imagem']['base64']
            v_indicadores['original']['dimensao']['altura']     =   v_altura
            v_indicadores['original']['dimensao']['largura']    =   v_largura
            # Inicia a construção do JSON de indicadores

            # Com a imagem em mãos ... inicia tratamento
            # Percorrerá o modelo de detecção em busca dos objetos
            for csr_aprendizado in self.VMBRAUNA_MODELO_TF:
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

                    # Coleta as informações obtidas - Somente as que geraram dimensões
                    for csr_iterador in range(0,len(np.squeeze(csr_dimensoes))):
                        # Apenas registros dentro dos padrões informados serão tratados
                        if ((np.squeeze(csr_pontuacao)[csr_iterador]) *100) >= p_json['corte']:

                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]
                            # (left, right, top, bottom)
                            vcx_alto        =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(1) * int(v_altura))    #  * v_altura
                            vcx_baixo       =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(3) * int(v_altura))
                            vcx_direita     =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(2)* int(v_largura))    # * v_largura
                            vcx_esquerda    =   int(np.squeeze(csr_dimensoes)[csr_iterador].item(0) * int(v_largura))
                            # Marca as dimensões para detecção  [ALTO - BAIXO - DIREITO - ESQUERDA]

                            # Desenha a área numa cópia para retorno
                            cv2.rectangle(v_imagem_retorno, (vcx_alto, vcx_direita), (vcx_baixo, vcx_esquerda), (self.VMBRAUNA_COR[v_indice_cor]["VERMELHO"], self.VMBRAUNA_COR[v_indice_cor]["AZUL"], self.VMBRAUNA_COR[v_indice_cor]["VERDE"]), 1)
                            # Desenha a área numa cópia para retorno

                            # Marca a tupla de elemento identificado
                            v_tmp_imagem_corte          =   self.func_imagem_para_base64(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo])
                            v_tmp_imagem_array          =   Imagem.fromarray(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo])
                            v_tmp_altura, v_tmp_largura =   v_tmp_imagem_array.size

                            # Gera os dados do dicionário de indicadores
                            v_indicador_dict['base64']              =   v_tmp_imagem_corte
                            v_indicador_dict['dimensao']['altura']  =   v_tmp_altura
                            v_indicador_dict['dimensao']['largura'] =   v_tmp_largura
                            v_indicador_dict['limite']['x1']        =   vcx_alto
                            v_indicador_dict['limite']['x2']        =   vcx_direita
                            v_indicador_dict['limite']['y1']        =   vcx_baixo
                            v_indicador_dict['limite']['y2']        =   vcx_esquerda
                            v_indicador_dict['cor']['Vermelho']     =   self.VMBRAUNA_COR[v_indice_cor]["VERMELHO"]
                            v_indicador_dict['cor']['Verde']        =   self.VMBRAUNA_COR[v_indice_cor]["VERDE"]
                            v_indicador_dict['cor']['Azul']         =   self.VMBRAUNA_COR[v_indice_cor]["AZUL"]

                            # Cria os dados do elemento identificado e suas respectivas pontuações
                            v_tmp_ret_elemento  =   {
                                                        'elemento'  :   csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize()
                                                       ,'pontuacao' :   ((np.squeeze(csr_pontuacao)[csr_iterador]) * 100)
                                                    }
                            # Adiciona o dado da identificação na array
                            if csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize() not in v_indicador_dict['descricao']:
                                v_indicador_dict['descricao'].append(csr_aprendizado['INDICE'][np.squeeze(csr_classe).astype(np.int32)[csr_iterador]]['name'].capitalize())
                                v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                            # Cria os dados do elemento identificado e suas respectivas pontuações
                            # Marca a tupla de elemento identificado


                            # Inicia detecção facial na imagem
                            for csr_deteccao_modelo in self.VMBRAUNA_MODELO_FACIAL:
                                # Verifica se houve sucesso no carregador do reconhecimento facial
                                if csr_deteccao_modelo['SUCESSO']:
                                    # Array para imagens escolhidas - Detectará a quantidade de rostos
                                    v_dimensao_reconhecida  =   csr_deteccao_modelo['METODO'].detectMultiScale(v_imagem[vcx_esquerda:vcx_direita, vcx_alto:vcx_baixo], scaleFactor=1.2, minNeighbors=(int(int(p_json['corte'])/10)))

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
                                            #cv2.rectangle(v_imagem_retorno, (v_alto, v_direita), (v_baixo, v_esquerda), (self.VCX_CORES[v_indice_cor]["VERMELHO"], self.VCX_CORES[v_indice_cor]["AZUL"], self.VCX_CORES[v_indice_cor]["VERDE"]), 1)
                                            # Desenha o objeto encontrado

                                            # Preparação para inserir a descrição
                                            # Verifica se o termo que será inserido já não foi detectado anteriormente
                                            # Adiciona o tipo
                                            if csr_deteccao_modelo['TIPO'].capitalize() not in v_indicador_dict['descricao']:
                                                # Cria os dados do elemento identificado e suas respectivas pontuações
                                                v_tmp_ret_elemento  =   {
                                                                            'elemento'  :   csr_deteccao_modelo['TIPO'].capitalize()
                                                                           ,'pontuacao' :   p_json['corte']
                                                                        }
                                                # Adiciona o dado da identificação na array
                                                v_indicador_dict['descricao'].append(csr_deteccao_modelo['TIPO'].capitalize())
                                                v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                                                # Cria os dados do elemento identificado e suas respectivas pontuações
                                            # Adiciona o subtipo
                                            if csr_deteccao_modelo['SUBTIPO'].capitalize() not in v_indicador_dict['descricao']:
                                                # Cria os dados do elemento identificado e suas respectivas pontuações
                                                v_tmp_ret_elemento  =   {
                                                                            'elemento'  :   csr_deteccao_modelo['SUBTIPO'].capitalize()
                                                                           ,'pontuacao' :   p_json['corte']
                                                                        }
                                                # Adiciona o dado da identificação na array
                                                v_indicador_dict['descricao'].append(csr_deteccao_modelo['SUBTIPO'].capitalize())
                                                v_indicador_dict['elemento'].append(v_tmp_ret_elemento)
                                                # Cria os dados do elemento identificado e suas respectivas pontuações
                            # Inicia detecção facial na imagem

                            v_indicadores['lista'].append(v_indicador_dict)

                            # Incrementa o contador de cores
                            v_indice_cor += 1       # Incrementa o índice de cores
                            if v_indice_cor > 99:   # Se o índice for superior à 99
                                v_indice_cor = 0    # Retorna ao registro inicial
                            # Incrementa o contador de cores
                        # Apenas registros dentro dos padrões informados serão tratados
            # Percorrerá o modelo de detecção em busca dos objetos

            # Marca a base64 e dimensões do resultado da imagem
            v_tmp_imagem_retorno    =   self.func_imagem_para_base64(v_imagem_retorno)
            v_imagem_array          =   Imagem.fromarray(v_imagem_retorno)
            v_altura, v_argura      =   v_imagem_array.size
            # Marca a base64 e dimensões do resultado da imagem

            # Gera os dados de imagem final
            v_indicadores['final']['base64']                =   v_tmp_imagem_retorno
            v_indicadores['final']['dimensao']['altura']    =   v_altura
            v_indicadores['final']['dimensao']['largura']   =   v_largura
            # Gera os dados de imagem final
            # INICIA O TRATAMENTO DA IMAGEM --------------------------------#

        except Exception  as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            v_indicadores       =   {
                                        'ERRO'  :   {
                                                        'TIPO'      :   'EXCPTN'
                                                       ,'MSG'       :   p_erro
                                                       ,'DETALHE'   :   {
                                                                            'TIPO'  :   ecx_tipo
                                                                           ,'NOME'  :   ecx_nome
                                                                           ,'LINHA' :   ecx_dados.tb_lineno
                                                                        }
                                                    }
                                    }
        except ValueError as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro

            v_indicadores       =   {
                                        'ERRO'  :   {
                                                        'TIPO'      :   'VLR'
                                                       ,'MSG'       :   p_erro
                                                       ,'DETALHE'   :   {
                                                                            'TIPO'  :   ecx_tipo
                                                                           ,'NOME'  :   ecx_nome
                                                                           ,'LINHA' :   ecx_dados.tb_lineno
                                                                        }
                                                    }
                                    }
        finally:
            return v_imagem_retorno
    # Função para reconhecimento de estruturas e faces

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

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

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função - Converte base64 para imagem
    def func_base64_para_imagem(self,p_base64):
        try:
            v_imagem_bytes  =   imread(io.BytesIO(base64.b64decode(p_base64)))
            v_imagem_final  =   cv2.cvtColor(v_imagem_bytes, cv2.COLOR_RGB2BGR)

            return v_imagem_final
        except Exception as p_erro:
            print(p_erro)
            return None
    # Função - Converte base64 para imagem

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função - Converte Imagem para base64
    def func_imagem_para_base64(self,p_imagem):
        try:
            v_dimensao, v_imagem    =   cv2.imencode('.jpg', p_imagem)
            v_img_bytes             =   base64.b64encode(v_imagem)
            v_img_string            =   v_img_bytes.decode()

            return v_img_string
        except Exception as p_erro:
            print(p_erro)
            return None
    # Função - Converte Imagem para base64

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Procedimento - Salva arquivo conforme informação recebida
    def proc_salva_arquivo(self, p_nome_arquivo, p_conteudo):
        try:
            if p_nome_arquivo is None:
                raise ValueError('O nome do arquivo e/ou caminho não identificado! Verifique.')

            if p_conteudo is None:
                raise ValueError('Conteúdo não inforado! Verifique.')
            # Abre o arquivo para escrita
            v_arquivo   =   open(p_nome_arquivo,'w')
            v_arquivo.write(p_conteudo)
            v_arquivo.close()
        except Exception  as p_erro:
            print(p_erro)
        except ValueError as p_erro:
            print(p_erro)
    # Procedimento - Salva arquivo conforme informação recebida

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para salvar imagem no banco de dados
    def func_salva_imagem(self, p_imagem, p_id_usuario):
        try:
            v_retorno       =   False
            # Transforma a imagem em base64 para salvar.
            v_imagem_base64 =   self.func_imagem_para_base64(p_imagem)
            # Transforma a imagem em base64 para salvar.

            # Adiciona a imagem à base realizando vínculo a um usuário
            v_tabela        =   'usuario_imagem'
            v_cursor        =   self.VMBRAUNA_CONEXAO.cursor()

            v_cursor.execute('insert into %s(id_usuario, base64) values(%s, %s)',v_tabela, p_id_usuario, v_imagem_base64)
            # Adiciona a imagem à base realizando vínculo a um usuário
        except Exception  as p_erro:
            v_retorno       =   False
            self.VMBRAUNA_CONEXAO.rollback()
        except ValueError as p_erro:
            v_retorno       =   False
            self.VMBRAUNA_CONEXAO.rollback()
        else:
            v_retorno       =   True
            self.VMBRAUNA_CONEXAO.commit()
        finally:
            v_cursor.close()
            return v_retorno
    # Função para salvar imagem no banco de dados

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para transformar dimensões DLIB em OPENCV
    def func_dimensao_dlib_opencv(p_dimensao):
        try:
            return rect.top(), rect.right(), rect.bottom(), rect.left()
        except Exception as e:
            return None, None, None, None
    # Função para transformar dimensões DLIB em OPENCV

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para transformar dimensões OpenCV em DLib
    def func_dimensao_opencv_dlib(p_dimensao):
        try:
            return dlib.rectangle(css[3], css[0], css[1], css[2])
        except Exception as e:
            return None
    # Função para transformar dimensões OpenCV em DLib

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para cortar as dimensões localizadas que estiverem excedendo a função inicial
    def func_aparar_dimensao(p_dimensao, p_img_original_dimensao):
        try:
            return max(p_dimensao[0], 0), min(p_dimensao[1], p_img_original_dimensao[1]), min(p_dimensao[2], p_img_original_dimensao[0]), max(p_dimensao[3], 0)
        except Exception as e:
            return None
    # Função para cortar as dimensões localizadas que estiverem excedendo a função inicial

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

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
            if len(p_rosto) == 0
                return np.empty((0))

            return np.linalg.norm(p_rosto - p_rosto_comparar,axis=1)
        except Exception  as p_erro:
            return np.empty((0))
        except ValueError as p_erro:
            return np.empty((0))
    # Função para detectar rostos com base em distância euclidiana faces similares

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

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

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função - Transforma array em Imagem
    def func_img_expandida_para_normal(self, p_imagem_expandida):
        try:
            return np.squeeze(p_array_imagem, axis=0)
        except Exception as e:
            return None
    # Função - Transforma array em Imagem


    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para converter imagem numpy em imagem OpenCV
    def func_imagem_numpy_para_opencv(p_imagem):
        try:
            return np.zeros(p_imagem, np.unit8)
        except Exception as p_erro:
            return None
        except Exception as p_erro:
            return None
    # Função para converter imagem numpy em imagem OpenCV


    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

    # Função para converter imagem opencv em imagem numpy
    def func_imagem_opencv_para_numpy(p_imagem):
        try:
            return np.asarray(p_imagem, dtype='uint8')
        except Exception as p_erro:
            return None
        except Exception as p_erro:
            return None
    # Função para converter imagem opencv em imagem numpy

    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #
    # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- # -><- #

# # --------------------------------------------------------------# #
