from sklearn.svm import SVR

class SGDRegression:

    def __init__(self):
        self.best_score = 100
        self.best_kernel = ''
        self.best_tol = 0
        self.best_clt = None

    def trainSVM(self, X, y, kernel='rbf', tol=1e-3):
        clf = SVR(kernel=kernel, tol=tol)
        clf.fit(X, y)   
        return clf

    def estimate(self, X_train, X_test, y_train, y_test):
        
        # Calibrando kernel
        self.best_score = 100
        for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
            for tol in [1e-3, 1e-4, 1e-5]:                
                clf = self.trainSVM(X_train, y_train, kernel, tol)
                score = clf.score(X_test, y_test)
                if abs(score) < abs(self.best_score):
                    self.best_score = score
                    self.best_kernel = kernel
                    self.best_tol = tol
                    self.best_clt = clf