# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

import  numpy                               as np
import  pprint
import  sys
from    mbrauna        import mbrauna       as mb

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

p_entrada                   =   np.array([[0., 0.],[0.,1.],[1.,0.],[1.,1.]])
p_classe                    =   np.array([[0.],[1.],[1.],[0.]])
p_epocas                    =   1
p_momentum                  =   1
p_tx_apr                    =   0.1
p_perceptron_camada_oculta  =   3
p_qtde_camada_oculta        =   1
p_qtde_saida                =   1

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

# Validação para os parâmetros necessários no procedimento
if p_entrada.size == 0:
    sys.exit()

if p_classe.size == 0:
    sys.exit()

if p_epocas     <= 0:
    sys.exit()

if p_momentum   <= 0:
    sys.exit()

if p_tx_apr     <= 0:
    sys.exit()

if p_perceptron_camada_oculta <= 0:
    sys.exit()

if p_qtde_camada_oculta < 0:
    sys.exit()

if p_qtde_saida <= 0:
    sys.exit()
# Validação para os parâmetros necessários no procedimento

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

# Declaração de variáveis
vgb_print                   =   pprint.PrettyPrinter(indent=10)

vgb_peso_entrada            =   np.array([])
vgb_peso_oculta             =   np.array([])
vgb_peso_saida              =   np.array([])
vgb_resultado               =   []

vgb_corpo_entrada           =   p_entrada.shape

vgb_dados                   =   dict()
vgb_chave_entrada           =   'entrada_'
vgb_chave_registro          =   'reg_'

vgb_erro                    =   0
vgb_mean_square_error       =   0
# Declaração de variáveis

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

# Criação dos pesos aleatórios
if p_qtde_camada_oculta <= 0:
    vgb_peso_entrada    =   np.random.rand((vgb_corpo_entrada[1],p_qtde_saida))
else:
    vgb_peso_entrada    =   np.random.rand(vgb_corpo_entrada[1],p_perceptron_camada_oculta) #[vtmp_array[cur_tmp_peso] for cur_tmp_peso in range(len(vtmp_array))]
    vgb_peso_oculta     =   np.random.rand(p_qtde_camada_oculta-1,p_perceptron_camada_oculta,p_perceptron_camada_oculta)#[vtmp_array[cur_tmp_peso] for cur_tmp_peso in range(len(vtmp_array))]
    vgb_peso_saida      =   np.random.rand(p_perceptron_camada_oculta, p_qtde_saida)#[vtmp_array[cur_tmp_peso] for cur_tmp_peso in range(len(vtmp_array))]
# Criação dos pesos aleatórios

# -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

# Executa as epocas para treinamento- p_epocas
for cur_epoca in range(p_epocas):
    # Limpa as variáveis para novos testes
    vgb_dados               =   dict()
    vgb_resultado           =   []

    vgb_erro                =   0
    vgb_mean_square_error   =   0
    # Limpa as variáveis para novos testes


    # --------------------------------------------------------------------------- #
    # Verifica as informações repassadas pelas entradas
    for cur_entrada in range(len(p_entrada)):
        # Cria um novo registro para esta entrada
        vgb_dados[vgb_chave_entrada + str(cur_entrada)]    =   dict()
        # Cria um novo registro para esta entrada

        # - Coleta os dados para cálculo - #
        vtmp_entrada        =   p_entrada[cur_entrada]
        vtmp_peso           =   vgb_peso_entrada
        # - Coleta os dados para cálculo - #

        # - Calcula a entrada dos dados - #
        vtmp_soma           =   np.dot(vtmp_entrada, vtmp_peso)
        vtmp_ativacao       =   np.array([mb.AtivacaoSigmoid(vtmp_soma[cur_soma]) for cur_soma in range(len(vtmp_soma))])
        # - Calcula a entrada dos dados - #

        # - Salva as informações para tratamento - #
        vgb_dados[vgb_chave_entrada + str(cur_entrada)][vgb_chave_registro + str(0)]    =   {
                                                                                                'Entrada'           :   vtmp_entrada
                                                                                               ,'Peso'              :   vtmp_peso
                                                                                               ,'Soma'              :   vtmp_soma
                                                                                               ,'Ativacao'          :   vtmp_ativacao
                                                                                               ,'DerivadaAtivacao'  :   mb.DerivadaSigmoid(vtmp_ativacao)
                                                                                            }
        # - Salva as informações para tratamento - #

        ## Subtrai-se 1 registro pois o último da camada oculta será direto para a camada de saída
        for cur_oculta in range(p_qtde_camada_oculta):
            if cur_oculta < p_qtde_camada_oculta-1:
                # - Coleta os dados para cálculo - #
                vtmp_entrada    =   vtmp_ativacao
                vtmp_peso       =   vgb_peso_oculta[cur_oculta]
                # - Coleta os dados para cálculo - #

                # - Calcula a entrada dos dados - #
                vtmp_soma       =   np.dot(vtmp_entrada, vtmp_peso)
                vtmp_ativacao   =   np.array([mb.AtivacaoSigmoid(vtmp_soma[cur_soma]) for cur_soma in range(len(vtmp_soma))])
                # - Calcula a entrada dos dados - #

                # - Salva as informações para tratamento - #
                vgb_dados[vgb_chave_entrada + str(cur_entrada)][vgb_chave_registro + str(cur_oculta+1)]     =   {
                                                                                                                    'Entrada'           :   vtmp_entrada
                                                                                                                   ,'Peso'              :   vtmp_peso
                                                                                                                   ,'Soma'              :   vtmp_soma
                                                                                                                   ,'Ativacao'          :   vtmp_ativacao
                                                                                                                   ,'DerivadaAtivacao'  :   mb.DerivadaSigmoid(vtmp_ativacao)
                                                                                                                }
                # - Salva as informações para tratamento - #

            else:
                # - Coleta os dados para cálculo - #
                vtmp_entrada    =   vtmp_ativacao
                vtmp_peso       =   vgb_peso_saida
                # - Coleta os dados para cálculo - #

                # - Calcula a entrada dos dados - #
                vtmp_soma       =   np.dot(vtmp_entrada, vtmp_peso)
                vtmp_ativacao   =   np.array([mb.AtivacaoSigmoid(vtmp_soma[cur_soma]) for cur_soma in range(len(vtmp_soma))])
                # - Calcula a entrada dos dados - #


                # - Salva as informações para tratamento - #
                vgb_dados[vgb_chave_entrada + str(cur_entrada)][vgb_chave_registro + str(cur_oculta+1)]     =   {
                                                                                                                    'Entrada'           :   vtmp_entrada
                                                                                                                   ,'Peso'              :   vtmp_peso
                                                                                                                   ,'Soma'              :   vtmp_soma
                                                                                                                   ,'Ativacao'          :   vtmp_ativacao
                                                                                                                   ,'Classe'            :   p_classe[cur_entrada]
                                                                                                                   ,'Erro'              :   ((p_classe[cur_entrada] - vtmp_ativacao) **2)
                                                                                                                   ,'MSE'               :   mb.ErroMSE(p_classe[cur_entrada], vtmp_ativacao)
                                                                                                                   ,'DerivadaAtivacao'  :   mb.DerivadaSigmoid(vtmp_ativacao)
                                                                                                                   ,'DeltaSaida'        :   mb.ErroMSE(p_classe[cur_entrada], vtmp_ativacao) * mb.DerivadaSigmoid(vtmp_ativacao)
                                                                                                                }
                # - Salva as informações para tratamento - #
    # Verifica as informações repassadas pelas entradas
    # --------------------------------------------------------------------------- #






    # --------------------------------------------------------------------------- #
    # Imprime os dados obtidos em vgb_dados
    #vgb_print.pprint(vgb_dados)
    # Imprime os dados obtidos em vgb_dados

    # - Coleta os erros da época - #
    vgb_resultado   =   np.array([vgb_dados[vgb_chave_entrada + str(cur_entrada)][vgb_chave_registro + str(len(vgb_dados[vgb_chave_entrada + str(cur_entrada)]) -1)]['Ativacao'] for cur_entrada in range(len(p_entrada))])
    # - Coleta os erros da época - #

    # - Imprime os dados obtidos em vgb_resultado - #
    #print(vgb_resultado)
    # - Imprime os dados obtidos em vgb_resultado - #

    # - Inicia a validação do erro para cálculo do backpropagation - #
    # - Inicia a validação do erro para cálculo do backpropagation - #
    # --------------------------------------------------------------------------- #






    # --------------------------------------------------------------------------- #
    # Percorre agora voltando até o primeiro registro e atualizando os pesos
    # BACKPROPAGATION - Atualização dos pesos
    # Levando em conta que todos os dados são simétricos
    # O tamanho poderá ser coletado em qualquer etapa, logo ... Obtenho da primeira, que é certeza sempre.
    vtmp_tamanho    =   len(vgb_dados[vgb_chave_entrada + str(0)])
    # O tamanho poderá ser coletado em qualquer etapa, logo ... Obtenho da primeira, que é certeza sempre.
    # Levando em conta que todos os dados são simétricos
    
    vgb_print.pprint(vgb_dados[vgb_chave_entrada + str(0)]['reg_0'])
    print('\n\n\n\n\n\n')
    vgb_print.pprint(vgb_dados[vgb_chave_entrada + str(0)]['reg_1'])
    #for cur_backpropagation in reversed(range(vtmp_tamanho)):
    # --------------------------------------------------------------------------- #


# Executa as epocas para treinamento- p_epocas