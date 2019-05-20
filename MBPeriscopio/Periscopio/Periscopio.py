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
#                                                                           #
#############################################################################
'''

# Bibliotecas necessárias para o processo de identificação de objetos
import numpy                                                            as np
# Bibliotecas necessárias para o processo de identificação de objetos


class periscopio_core(object):
    '''
    FONT_HERSHEY_SIMPLEX = 0,
    FONT_HERSHEY_PLAIN = 1,
    FONT_HERSHEY_DUPLEX = 2,
    FONT_HERSHEY_COMPLEX = 3,
    FONT_HERSHEY_TRIPLEX = 4,
    FONT_HERSHEY_COMPLEX_SMALL = 5,
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
    FONT_HERSHEY_SCRIPT_COMPLEX = 7,
    FONT_ITALIC = 16
    '''
    PERISCOPIO_FONTE    =   cv2.FONT_ITALIC
    PERISCOPIO_CONFIG   =   None

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def carrega_cor(self):
        '''
        Autor: Michel Brauna           Data: 27/01/2011

        Procedimento para carregamento de cores a serem
        utilizadas na detecção.
        '''

        try:
            # Gera cores aleatórias no padrão RGB - Carrega dicionário
            vmb_tmp_cor         =   {}

            vmb_tmp_cor['R']    =   int(np.random.randint(0,255))
            vmb_tmp_cor['G']    =   int(np.random.randint(0,255))
            vmb_tmp_cor['B']    =   int(np.random.randint(0,255))
            vmb_tmp_cor['RGB']  =   '#%02x%02x%02x' % (vmb_tmp_cor['R'], vmb_tmp_cor['G'], vmb_tmp_cor['B'])
            # Gera cores aleatórias no padrão RGB - Carrega dicionário

            # Adiciona a lista de cores conhecidas
            self.PERISCOPIO_CONFIG['CORES'].append(vmb_tmp_cor)
            # Adiciona a lista de cores conhecidas
        except Exception as p_erro:
            # Mais detalhes sobre o erro
            ecx_tipo, ecx_obj, ecx_dados    =   sys.exc_info()
            ecx_nome                        =   os.path.split(ecx_dados.tb_frame.f_code.co_filename)[1]
            # Mais detalhes sobre o erro
            vtmp_mensagem                   =   'Erro: ' + p_erro + '\n\n\nLinha:' + ecx_dados.tb_lineno;
            if (('Log' in self.PERISCOPIO_CONFIG) && ('Config in self.PERISCOPIO_CONFIG')):
                # Escreve a mensagem para salvar no log de messageria                
                self.PERISCOPIO_CONFIG['Log'].mensagem(self.PERISCOPIO_CONFIG['Config'],vtmp_mensagem);
                # Escreve a mensagem para salvar no log de messageria

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def carrega_tensores(self):
        try:
            # Marca as versões para o modelo, descrição e patches
            for csr_modelo_tensor in self.PERISCOPIO_CONFIG['Modelo']['Tensor']:
                try:
                    vmb_tmp_modelo          =   {}

                    # Carrega o modelo para o ambiente Tensorflow
                    v_caminho_deteccao      =   os.path.join()                                          # Marca o caminho que será utilizado para a predição e detecção de classes de imagens
                    v_caminho_descricao     =   os.path.join()                                          # Marca a descrição dos patches encontrados na detecção
                    # Carrega o modelo para o ambiente Tensorflow

                    # Gera o modelo para o tensor - Periscópio
                    v_mapa_elemento         =   cx_desc.load_labelmap(v_caminho_descricao)
                    v_categoria             =   cx_desc.convert_label_map_to_categories(v_mapa_elemento,max_num_classes=90,use_display_name=True)
                    v_indice_categoria      =   cx_desc.create_category_index(v_categoria)
                    # Gera o modelo para o tensor - Periscópio

                    # Por fim, cria o treino necessário do tensor
                    v_treino                =   tf.Graph()

                    with v_treino.as_default():
                        v_definicao         =   tf.GraphDef();

                        with tf.gfile.GFile(v_caminho_deteccao,'rb') as fid:
                            v_serializacao  =   fid.read()
                            v_definicao.ParseFromString(v_serializacao)
                            tf.import_graph_def(v_definicao, name='')

                        # Após tratada todas as definições ...
                        # Gera a sessão final ..
                        v_sessao            =   tf.Session(graph=v_treino)
                        # Após tratada todas as definições ...
                    # Por fim, cria o treino necessário do tensor



                except Exception as p_tmp_erro:
                    raise e
            # Marca as versões para o modelo, descrição e patches
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #