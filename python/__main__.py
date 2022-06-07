###################################################################### ATIVIDADE 13 ####################################################################
#
#   - carregue os 2 arquivos em anexo para um banco de dados
#   - leia do banco em blocos de 50 dados, ordenados por data
#   - para cada bloco registre em uma tabela própria a média, mediana, moda, desvio padrão, maior e menor valores do bloco,
#     data de início e data de fim do bloco
#   - salvar no banco de dados todos os registros e logs de todas as operações realizadas(SGBD/Python), armazenado quem fez, quando fez e o que fez.
#
########################################################################################################################################################

from modules.connector import interface_db
import pandas as pd
import statistics 


if __name__ == "__main__":
    
    """ SELECIONA TABELA 'DADOS' DO BD ATIVIDADE13
    """
    try:
        query= "SELECT * FROM dados;"
        dados = interface_db.buscar(query) 
    except Exception as e:
        print("Erro ao selecionar tabela do banco --> ", e)
        
       
    """ TRANSFORMA A TABELA EM DATAFRAME
    """ 
    try:
        dados_from_pg = pd.DataFrame(dados) 
        dados_from_pg = dados_from_pg.drop(columns=[0])
        dados_from_pg[2] = dados_from_pg[2].apply(float)    # TRANSFORMA VALORES DA COLUNA 2 EM FLOAT
       
    except Exception as e:
        print("Erro nos cálculos --> ", e)
        
    
    """ LEITURA DA TABELA EM BLOCOS DE 50 DADOS, 
        CALCULOS DOS VALORES DOS BLOCOS, 
        E INSERCAO DOS RESULTADOS NA TABELA 'CALCULOS'
    """
    try:   
        for i in range(0, len(dados_from_pg), 49):          # LEITURA DA TABELA EM BLOCOS
            dados_sliced = dados_from_pg.iloc[i : i + 49]

            # CALCULO MEDIA       
            try:     
                dados_media = dados_sliced[2].mean()       
            except Exception as e:
                print("Erro no calculo da media --> ", e)
                
            # CALCULO MEDIANA       
            try:   
                dados_mediana = dados_sliced[2].median()        
            except Exception as e:
                print("Erro no calculo da mediana --> ", e)
                
            # CALCULO DA MODA    
            try:    
                dados_moda = statistics.mode(dados_sliced[2])      
            except Exception as e:
                print("Erro no calculo da moda --> ", e)
            
            # CALCULO DO DESVIO PADRAO
            try:    
                dados_desvio_padrao = dados_sliced[2].std()         
            except Exception as e:
                print("Erro no calculo do desvio padrao --> ", e)
            
            # APONTAMENTO DO VALOR MAX DO BLOCO
            try:    
                dados_max = dados_sliced[2].max()       
            except Exception as e:
                print("Erro no apontamento do maior valor do bloco --> ", e)
            
            # APONTAMENTO DO VALOR MIN DO BLOCO
            try:
                dados_min = dados_sliced[2].min()       
            except Exception as e:
                print("Erro no apontamento do menor valor do bloco --> ", e)
            
            # DATA INICIO DO BLOCO
            try:
                data_inicio = dados_sliced[1].max()     
            except Exception as e:
                print("Erro no apontamento da data de inicio do bloco --> ", e)
            
            # DATA FIM DO BLOCO
            try:
                data_fim = dados_sliced[1].min()        
            except Exception as e:
                print("Erro no apontamento da data de fim do bloco --> ", e)
            
            # INSERCAO DOS RESULTADOS NA TABELA 'CALCULOS'
            try:    
                query = """INSERT INTO calculos(media, mediana,moda,desvio_padrao, maior_valor, menor_valor, data_inicio, data_fim) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
                """% (dados_media, dados_mediana, dados_moda, dados_desvio_padrao, dados_max, dados_min, data_inicio, data_fim)
                interface_db.inserir_db(query)
            except Exception as e:
                print("Erro insercao de resultados dos calculos -->", e)
            
            
    except Exception as e:
        print("Erro ao criar blocos -->", e)
        

    
    