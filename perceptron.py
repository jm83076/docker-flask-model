# Import dependencies
import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_iris

#load iris dataset
iris=load_iris()

#make a dataset with loaded values
df = pd.DataFrame(data = np.c_[iris['data'], iris['target']], 
                  columns=iris['feature_names']+['target'])


#delete rows with value 2 in target column

#df = df[df['target'] != 2]

#split columns to features columns and target column
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

#creating an easy ann model - perceptron
class Perceptron:
    
    def __init__(self, eta=0.01, n_iter=30):
        self.eta = eta
        self.n_iter = n_iter
        self.w_ = None
        self.errors_ = None
    
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def _net_input(self, X):
        X = np.squeeze(np.asarray(X))
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self._net_input(X) >= 0, 1, -1)
    



#training a model
model = Perceptron()
model.fit(X,y)

#saving created model
with open("model_perc.pkl", "wb") as model_1:
    pickle.dump(model, model_1)

