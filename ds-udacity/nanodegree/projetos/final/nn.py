from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

class NN:
    
    def baseline_model(self):
        # create model
        self.model = Sequential()
        self.model.add(Dense(28, input_dim=14, activation='relu'))
        self.model.add(Dense(56, activation='relu'))
        self.model.add(Dense(28, activation='relu'))
        self.model.add(Dense(1, activation='linear'))
        # Compile model
        self.model.compile(loss='mse', optimizer='adam')
    
    def fit(self, X, y, epochs, batch_size, verbose):
        self.scalarX = MinMaxScaler()
        self.scalarY = MinMaxScaler()

        self.scalarX.fit(X)
        self.scalarY.fit(y.values.reshape(y.shape[0], 1))

        X_t = self.scalarX.transform(X)
        y_t = self.scalarY.transform(y.values.reshape(y.shape[0], 1))
        self.model.fit(X_t, y_t, epochs=epochs, batch_size=batch_size, verbose=verbose)

    def predict(self, X):
        X_t = self.scalarX.transform(X)
        y_t = self.model.predict(X_t)
        return self.scalarY.inverse_transform(y_t)