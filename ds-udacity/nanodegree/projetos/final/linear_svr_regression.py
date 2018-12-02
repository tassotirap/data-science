from sklearn.svm import LinearSVR

class LinearSVRRegression:

    def __init__(self):
        self.best_epsilon = 0
        self.best_tol = 0
        self.best_clt = None

    def trainLinearSVR(self, X, y, tol, epsilon):
        clf = LinearSVR(random_state=0, tol=tol, epsilon=epsilon)
        clf.fit(X, y)   
        return clf

    def estimate(self, X_train, X_test, y_train, y_test):
        
        # Calibrando kernel
        self.best_score = 100
        for tol in [1e-3, 1e-4, 1e-5]:
            for epsilon in [0.1, 0.01, 0.001, 0.0001]:
                
                clf = self.trainLinearSVR(X_train, y_train, tol, epsilon)
                score = clf.score(X_test, y_test)

                if abs(score) < abs(self.best_score):
                    self.best_score = score
                    self.best_epsilon = epsilon
                    self.best_tol = tol
                    self.best_clt = clf