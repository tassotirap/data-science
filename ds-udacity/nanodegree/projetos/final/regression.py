from sklearn.linear_model import SGDRegressor

class Regression:
    
    def __init__(self):
        self.best_max_iter = 0
        self.best_tol = 0
        self.best_penalty = ''
        self.best_alpha = 0
        self.best_learning_rate = ''
        self.best_score = 100
        self.best_clt = None
    
    def trainRegression(self, X, y, max_iter=10000, tol=1e-3, penalty='l2', alpha=0.0001, learning_rate='invscaling'):
        
        clf = SGDRegressor(max_iter=max_iter, 
                           tol=tol,
                           penalty=penalty,
                           alpha=alpha,
                           learning_rate=learning_rate,
                           random_state=0)
        clf.fit(X, y)   

        return clf
    
    def estimate(self, X_train, X_test, y_train, y_test):
        
        # Calibrando max_iter, tol e penalty        
        self.best_score = 100        
        for max_iter in [10, 100, 1000, 10000]:
            for tol in [1e-3, 1e-4, 1e-5]:
                for penalty in ['none', 'l2', 'l1', 'elasticnet']:
                    clf = self.trainRegression(X_train, y_train, max_iter, tol, penalty)
                    score = clf.score(X_test, y_test)
                    if abs(score) < abs(self.best_score):
                        self.best_score = score
                        self.best_max_iter = max_iter
                        self.best_tol = tol
                        self.best_penalty = penalty

        # Calibrando alpha e learning_rate        
        self.best_score = 100        
        for alpha in [1e-5, 1e-6, 1e-7, 1e-20]:
            for learning_rate in ['constant', 'optimal', 'invscaling', 'adaptive']:
                clf = self.trainRegression(X_train, y_train, self.best_max_iter, self.best_tol, self.best_penalty, alpha, learning_rate)
                score = clf.score(X_test, y_test)
                if abs(score) < abs(self.best_score):
                    self.best_score = score
                    self.best_alpha = alpha
                    self.best_learning_rate = learning_rate     
                    self.best_clt = clf               