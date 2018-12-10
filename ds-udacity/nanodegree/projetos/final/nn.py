from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from keras import optimizers

class NN:
    
    def baseline_model(self, imput_size):
        # create model
        self.model = Sequential()
        self.model.add(Dense(imput_size, input_dim=imput_size, kernel_initializer='normal', activation='relu'))
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dense(1))
        # Compile model
        self.model.compile(loss='mse', optimizer=optimizers.Adadelta(), metrics=['accuracy'])
    
    def fit(self, X, y, epochs, batch_size, verbose):
        self.scalarX = MinMaxScaler()
        self.scalarY = MinMaxScaler()

        self.scalarX.fit(X)
        self.scalarY.fit(y.values.reshape(y.shape[0], 1))

        X_t = self.scalarX.transform(X)
        y_t = self.scalarY.transform(y.values.reshape(y.shape[0], 1))
        
        self.history = self.model.fit(X_t, y_t, epochs=epochs, validation_split = 0.2, batch_size=batch_size, verbose=verbose, shuffle=True)

    def predict(self, X):
        X_t = self.scalarX.transform(X)
        y_t = self.model.predict(X_t)
        return self.scalarY.inverse_transform(y_t)

    def save_weights(self, file_name):
        self.model.save_weights(file_name + '.h5')
        joblib.dump(self.scalarX, file_name + '.max_x')
        joblib.dump(self.scalarY, file_name + '.max_y')

    def load_weights(self, file_name):
        self.model.load_weights(file_name + '.h5')
        self.scalarX = joblib.load(file_name + '.max_x')
        self.scalarY = joblib.load(file_name + '.max_y')