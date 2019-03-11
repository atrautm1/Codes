# LDA
# Used some of the solutions from: https://sebastianraschka.com/Articles/2014_python_lda.html#step-1-computing-the-d-dimensional-mean-vectors
import pandas as pd
import random
import numpy as np
import math
from scipy.stats import zscore

class LDA():

    def __init__(self,data,y, normalize):
        self.X, self.y, self.m = self.__prepData(data,y,normalize)
        
    def __prepData(self,data,y, normalize):
        # Splitting x and y
        y_normalized = data.iloc[:, y-1:y].values # Takes pandas dataframe and turns into a numpy array
        if normalize:
            x_normalized = data.drop(data.iloc[:, y-1:y],axis=1).apply(zscore).values # Remove dependent variable and then calculate z-scores
        else:
            x_normalized = data.drop(data.iloc[:, y-1:y],axis=1).values
        #x_normalized = np.concatenate((np.zeros([0,x_normalized.shape[1]]),x_normalized),axis=0) # Add dummy x's
        # Define initial parameters
        m = len(data.index) # length of dataset
        return x_normalized, y_normalized, m

    def __bcs(self,d_var,x_means,x_sep,xm): # Between Class scatter
        S_b = np.zeros((d_var,d_var))
        for i,x in enumerate(x_means):
            n_i = len(x_sep[i])
            x = x.reshape(d_var,1)
            S_b += n_i * (x - xm) @ (x - xm).T
        return S_b

    def __wcs(self, d_var, x_sep, x_means):
        S_i = np.zeros((d_var,d_var))
        for i,x in enumerate(x_sep):
            for r in x:
                r, xnm = r.reshape(d_var,1), x_means[i].reshape(d_var,1)
                S_i += (r-xnm) @ (r-xnm).T
        return S_i

    def __calcEigenVals(self, S_i, S_b):
        ev, e = np.linalg.eig(np.linalg.inv(S_i) @ S_b)
        eigenPairs = [(np.abs(ev[i]), e[:,i]) for i in range(len(ev))]
        eigenPairs = sorted(eigenPairs,key=lambda k: k[0],reverse=True) # Sort the eigen pairs from largest eigen value to lowest
        self.p0 = eigenPairs[0][0]
        self.p1 = eigenPairs[1][0]
        return eigenPairs

    def fit(self):
        x_sep = [] # Define list of variables separated by class
        cl = np.unique(self.y) # classes defined by the y variable
        d_var = self.X.shape[1]
        x_means = [] # Class variable means
        for i,l in enumerate(cl):
            x_sep.append(self.X[np.where(np.any(self.y == l, axis=1))])
            x_means.append(np.mean(x_sep[i], axis=0))
        xm = (np.mean(self.X, axis=0)).reshape(d_var,1) # Mean of total variables
        S_b = self.__bcs(d_var,x_means,x_sep,xm) # Calculate Between Class Scatter
        S_i = self.__wcs(d_var,x_sep,x_means) # Calculate Within Class Scatter
        eigenPairs = self.__calcEigenVals(S_i,S_b) # Calculate eigenvalues and eigenvectors
        self.W = np.hstack((eigenPairs[0][1].reshape(d_var,1), eigenPairs[1][1].reshape(d_var,1)))
        self.x_sep = x_sep
        return self.W
    
    def predict(self,data,y,normalize):
        X, y, _ = self.__prepData(data,y,normalize)
        return X @ self.W


if __name__ == "__main__":
    toyDS = pd.read_csv('/Users/atrautm1/Downloads/toy_data_for_LDA.csv')
    a = LDA(toyDS,3,True)
    a.fit()
    #a.fit()
    #print(a.output)