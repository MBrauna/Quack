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
import os
import psycopg2
import pymysql
import sys
import quackserver
# Bibliotecas para conexão ao banco de dados


class quackdb:
    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # Inicializa o modelo QuackDB - Modelo Quack
    def __init__(self, p_configuracao):
        try:
            # Carrega os dados à partir da conexão necessária
            if p_configuracao['DB']['Tipo']     ==  0:
                vdb_conexao         =   psycopg2.connect(host       =   p_configuracao['DB']['Hospedeiro']
                                                        ,port       =   p_configuracao['DB']['Porta']
                                                        ,user       =   p_configuracao['DB']['Usuario']
                                                        ,password   =   p_configuracao['DB']['Senha']
                                                        ,dbname     =   p_configuracao['DB']['Banco']
                                                        )

            elif p_configuracao['DB']['Tipo']   ==  1:
                vdb_conexao         =   pymysql.connect(host        =   p_configuracao['DB']['Hospedeiro']
                                                       ,port        =   p_configuracao['DB']['Porta']
                                                       ,user        =   p_configuracao['DB']['Usuario']
                                                       ,passwd      =   p_configuracao['DB']['Senha']
                                                       ,db          =   p_configuracao['DB']['Banco']
                                                       )
            # Carrega os dados à partir da conexão necessária

            return vdb_conexao
        except Exception as p_erro:
            return None
    # Inicializa o modelo QuackDB - Modelo Quack

    # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- # -- #

    # QuackDB - Realiza consulta
    
    # QuackDB - 

        
