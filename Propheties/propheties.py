'''
Autor: Michel Brauna                        Data: 22/05/2019

Classe para geração de predição de valores e dados 
'''

# Biblioteca de métodos para propheties
import math
import numpy as np
# Biblioteca de métodos para propheties


class propheties:

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #
    VMB_TAXA_APRENDIZADO    =   0.1
    VMB_EPOCA               =   10000
    VMB_CAMADA_OCULTA       =   1
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def funcao_soma(self, p_entrada, p_peso):
        try:
            # Cria uma array contendo a multiplicação de todos os valores obtidos
            # Soma todos os resultados
            return sum([p_entrada[curreg] * p_peso[curreg] for curreg in range(len(p_entrada))])

        except Exception as e:
            return 0

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def funcao_sigmoid(self, p_entrada):
        try:
            return (1/(1 + (math.exp(-p_entrada))))
        except Exception as e:
            return 0

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    def funcao_treino(self, p_lista, p_resultado, p_camada_oculta):
        # Coleta os dados do tamanho da lista para tratamento
        v_tamanho_lista     =   len(p_lista)
        v_qtde_entrada      =   len(p_lista[0])
        # Coleta os dados do tamanho da lista para tratamento

        # Verifica a quantidade de entradas iniciais
        for cur_epoca in range(self.VMB_EPOCA):
        # [FIM] - for cur_epoca in range(self.VMB_EPOCA):
        # Verifica a quantidade de entradas iniciais

