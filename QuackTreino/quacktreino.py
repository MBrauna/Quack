"""
Autor: Michel Brauna                                       Data: 16/03/2019

Modelo de treino para novos tipos de detecção, o treino consiste em obter o XML das marcações obtidas
no sistema LabelIMG e repassá-las à estrutura normal do tensorflow.

             ██████╗ ██╗   ██╗ █████╗  ██████╗██╗  ██╗     
            ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║ ██╔╝     
            ██║   ██║██║   ██║███████║██║     █████╔╝      
            ██║▄▄ ██║██║   ██║██╔══██║██║     ██╔═██╗      
            ╚██████╔╝╚██████╔╝██║  ██║╚██████╗██║  ██╗     
             ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     
                                                           
            ████████╗██████╗ ███████╗██╗███╗   ██╗ ██████╗ 
            ╚══██╔══╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗
               ██║   ██████╔╝█████╗  ██║██╔██╗ ██║██║   ██║
               ██║   ██╔══██╗██╔══╝  ██║██║╚██╗██║██║   ██║
               ██║   ██║  ██║███████╗██║██║ ╚████║╚██████╔╝
               ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

# Bibliotecas para uso no treino QUACK

import  argparse
import  glob
import  os
import  pandas as pd
import  sys
import  xml.etree.ElementTree as ET
# Bibliotecas para uso no treino QUACK




class quacktreino:

    QUACKTREINO_CAMINHO     =   {
                                    'Entrada'   :   None
                                    'Descricao' :   None
                                    'Saida'     :   None
                                }



    # Inicialização do método Quack para tratamento dos dados e inicialização dos treinos
    def __init__(self, p_caminho_entrada, p_caminho_pbtxt, p_caminho_saida):
        print('[LEMBRETE] - Utilize do LabelIMG para facilitar a geração das áreas de detecção!')
        print('[LEMBRETE] - Atenção, use do XML gerado e do PBTXT adequado.')

        if p_caminho_entrada is None:
            print('[ERRO] Caminho de entrada não definido! Verifique.')
            sys.exit()

        if p_caminho_saida is None:
            print('[ERRO] Caminho de saida não definido! Verifique.')
            sys.exit()

        if p_caminho_pbtxt is None:
            print('[ERRO] Caminho do PBTXT não definido! Verifique.')
            sys.exit()

    # ----------------------------------------------------------------------------------------------- #

    def transforma_xml_csv():
        try:
            xml_list = []
                for xml_file in glob.glob(self.QUACKTREINO_CAMINHO['Entrada'] + '/*.xml'):
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    for member in root.findall('object'):
                        value = (root.find('filename').text,
                                int(root.find('size')[0].text),
                                int(root.find('size')[1].text),
                                member[0].text,
                                int(member[4][0].text),
                                int(member[4][1].text),
                                int(member[4][2].text),
                                int(member[4][3].text)
                                )
                        xml_list.append(value)
                column_name = ['filename', 'width', 'height',
                            'class', 'xmin', 'ymin', 'xmax', 'ymax']
                xml_df = pd.DataFrame(xml_list, columns=column_name)
                return xml_df
        except Exception as p_erro:
            # Finaliza o procedimento ...
            print('Não foi possível compor o CSV[',p_erro,']')
            sys.exit()

    # ----------------------------------------------------------------------------------------------- #

    def transforma_csv_record():