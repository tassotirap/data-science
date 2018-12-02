import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


class DataTransform:
    def __init__(self):
        self.processor = MinMaxScaler()
        self.pca = PCA(n_components=2)

    # Gerar Dummis das colunas de texto
    def getDummies(self, df):
        return pd.get_dummies(df)

    def fitNormalizeData(self, df):
        self.processor.fit(df)

    # Normalizar os dados númericos
    def normalizeData(self, df):
        scaled = self.processor.transform(df)
        return scaled

    def denormalizeData(self, df):
        unscaled = self.processor.inverse_transform(df)
        return unscaled

    def aplyPCA(self, df):
        pca_transform = self.pca.fit_transform(df)
        return pd.DataFrame(pca_transform, columns=['x1', 'x2'])

    def train_test_split(self, df):
        features = df.drop(columns=['PASSAGEIROS'])
        values = df['PASSAGEIROS']
        return train_test_split(features, values, test_size=0.2, random_state=0)
