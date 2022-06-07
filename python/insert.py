from modules.connector import interface_db
import pandas as pd

"""CODIGO PARA INSERIR DATAFRAME NO BANCO DE DADOS 
"""

# LE O ARQUIVO CSV
try:    
    dados = pd.read_csv("./dados_tratados.csv", sep = ",")
    dados_pg = pd.DataFrame(dados)
except Exception as e:
    print("Erro ao importar csv com dados tratados --> ", e)
    
# EXPORTA DATAFRAME PARA TABELA 'DADOS' NO BANCO 'ATIVIDADE13'
try:
        for i in dados_pg.index:
            query = """ INSERT INTO dados (datas_dados, valor_dados) VALUES ('%s', '%s');
            """% (dados_pg['data'][i],dados_pg['valor'][i])
            interface_db.inserir_db(query)
except Exception as e:
    print("Erro ao inserir dataframe no BD --> ", e)