import pandas as pd
import numpy as np

class DataClear:

    # Método para ler ados dos Voos de 2000 até 2018
    def readData(self, fileName): 
        return pd.read_csv(fileName, sep=';', encoding='utf-8')

    # Método os dados de voos com origem diferente de Brasil
    def clearNotBrazilianFlights(self, df):
        return df[df['AEROPORTO DE ORIGEM (PAÍS)'] == 'BRASIL']

    # Gerar colunas novas
    def createColumns(self, df):
        df['ASSENTOS'] = df['ASSENTOS'] / df['DECOLAGENS']
        df['INTER'] = df['AEROPORTO DE DESTINO (PAÍS)'] != 'BRASIL' 
        df['PASSAGEIROS_VOO'] = (df['PASSAGEIROS PAGOS'] + df['PASSAGEIROS GRÁTIS']) / df['DECOLAGENS']    
        df['PASSAGEIROS_TOTAL'] = (df['PASSAGEIROS PAGOS'] + df['PASSAGEIROS GRÁTIS'])
        return df

    # Método para remover as colunas que não iremos utilizar
    def removeNotUsedColumns(self, df):
        return df.drop([
            'EMPRESA (SIGLA)', 
            'EMPRESA (NOME)', 
            'EMPRESA (NACIONALIDADE)', 
            'AEROPORTO DE ORIGEM (SIGLA)', 
            'AEROPORTO DE ORIGEM (NOME)',
            'AEROPORTO DE ORIGEM (UF)',
            'AEROPORTO DE ORIGEM (PAÍS)',
            'AEROPORTO DE ORIGEM (CONTINENTE)',
            'AEROPORTO DE DESTINO (SIGLA)',
            'AEROPORTO DE DESTINO (NOME)',
            'AEROPORTO DE DESTINO (UF)',
            'AEROPORTO DE DESTINO (REGIÃO)',
            'AEROPORTO DE DESTINO (PAÍS)',
            'NATUREZA',
            'GRUPO DE VOO',
            'ASK',
            'RPK',
            'ATK',
            'RTK',
            'COMBUSTÍVEL (LITROS) - APENAS EMPRESAS BRASILEIRAS',
            'CARGA GRATIS KM',
            'CORREIO KM',
            'PAYLOAD',
            'HORAS VOADAS',
            'BAGAGEM (KG)',
            'CORREIO (KG)',
            'CARGA PAGA KM',
            'PASSAGEIROS PAGOS', 
            'PASSAGEIROS GRÁTIS', 
            'CARGA PAGA (KG)', 
            'CARGA GRÁTIS (KG)', 
            'DISTÂNCIA VOADA (KM)',
            'ASSENTOS',
            'DECOLAGENS',
            'PASSAGEIROS_VOO'
            ], axis=1)

    # Renomendo as colunas
    def renameColumsn(self, df):
        df.columns = ['ANO', 'MES', 'ORIGEM', 'DESTINO', 'INTER', 'PASSAGEIROS']
        return df

    def clearData(self, df):
        df = df[~np.isnan(df['ASSENTOS'])]
        df = df[~np.isnan(df['PASSAGEIROS_VOO'])]
        df = df[~np.isnan(df['DECOLAGENS'])]
        df = df[df['ASSENTOS'] > 90] # mínimo de 120 lugares (aviões comerciais)
        df = df[df['PASSAGEIROS_VOO'] > 30] # mínimo de 30 (aviões comerciais)
        df = df[df['DECOLAGENS'] > 0]
        return df

    def convertTypes(self, df):
        df['PASSAGEIROS'].astype('int64')
        return df

    def groupBy(self, df):
        return df.groupby(['ANO', 'MES', 'ORIGEM', 'DESTINO', 'INTER'], as_index=False).sum()