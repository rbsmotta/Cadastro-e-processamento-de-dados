import pandas as pd

""" CODIGO PARA LEITURA DO ARQUIVO CSV E
    TRATAMENTO DOS DADOS A SEREM EXPORTADOS PARA O BD
"""

try:

    try:    #LEITURA DOS DADOS NOS ARQUIVOS CSV
        path1 = '/home/robson/repositorios/atividades-soulcode/atividades_soulcode_academy/atividade-13/dados/DADOS_1.csv'
        path2 = '/home/robson/repositorios/atividades-soulcode/atividades_soulcode_academy/atividade-13/dados/DADOS_2.csv'
       
        df_dados1 = pd.read_csv(path1, sep = ";")     
        df_dados2 = pd.read_csv(path2, sep = ";")     
    except Exception as e:
        print("Erro ao ler arquivos .csv --> ", e)
        
    try:    # DROP DAS LINHAS QUE NAO CONTEM DADOS
        df_dados1 = df_dados1.dropna()     
        df_dados2 = df_dados2.dropna()     
    except Exception as e:
        print("Erro ao deletar linhas sem dados --> ", e)
         
    try:    # DROP DA COLUNA ID
        df_dados1.drop(["id"], axis=1, inplace=True) 
        df_dados2.drop(["id"], axis=1, inplace=True)  
    except Exception as e:
        print("Erro ao dropar coluna ID --> ", e)       
                
    try:    # CONCATENACAO DOS DATAFRAMES
        df_dados = pd.concat([df_dados1, df_dados2])    
    except Exception as e:
        print("Erro ao concatenar dataframe --> ", e)   
      
    try:    # ALTERANDO FORMATO DA DATA PARA DATETIME
        df_dados["data"] = pd.to_datetime(df_dados['data'])    
    except Exception as e:
        print("Erro ao mudar formato da data --> ", e)
        
    try:    # REORGANIZANDO FORMATO DATA PARA ANO/MES/DIA
        df_dados["data"] = df_dados["data"].dt.strftime('%Y/%m/%d')     
    except Exception as e:
        print("Erro ao reorganizar o formato da data --> ", e)
        
    try:    # ORDENANDO DATAFRAME POR DATA (DATA MAIS RECENTE PARA MAIS ANTIGA)
        df_dados_ordenados = df_dados.sort_values(by=["data"], ascending=False)    
    except Exception as e:
        print("Erro ao ordenar dataframe --> ", e)
    
    try:    # CRIANDO ARQUIVOS CSV
        df_dados_ordenados.to_csv('dados_tratados.csv', index=False)
    except Exception as e:
        print("Erro ao criar arquivo csv --> ", e)     
          
except Exception as e:
    print(str(e))



