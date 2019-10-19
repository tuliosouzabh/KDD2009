import pandas as pd

class Utils:
    
    def verifica_coluna(colunas, total):
        df = df
        for coluna in colunas:
        nacoluna = df[coluna].isna().value_counts()
        nacoluna = 1-(nacoluna[0] / total )
        print('Numero de Na na coluna', coluna, ' ',nacoluna)