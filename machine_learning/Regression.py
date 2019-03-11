
import pandas as pd
import random
import numpy as np
import math
from scipy.stats import zscore
# Borrowed some of the solution from: https://medium.com/we-are-orb/multivariate-linear-regression-in-python-without-scikit-learn-7091b1d45905
# Takes a pandas dataframe and performs a multivariate linear regression on it
# data is the dataframe
# y is the numerical column
# alpha is the alpha value by which the gradient will descend or ascend ( ie the learning rate )
# model is the regression model you want to use (either linear or log)
# delta_j_threshold is the lowest change in j that is acceptable
# regularize is the lambda value for regularization (if you want to not use regularization use; regularize=0)

class Regression():

    def __init__(self,data,y, normalize):
        self.X, self.y, self.m = self.__prepData(data,y,normalize)

    def __prepData(self,data,y, normalize):
        # Splitting x and y
        y_normalized = data.iloc[:, y-1:y].values # Takes pandas dataframe and turns into a numpy array of zscore values
        if normalize:
            x_normalized = data.drop(data.iloc[:, y-1:y],axis=1).apply(zscore).values # Remove dependent variable and then calculate z-scores
        else:
            x_normalized = data.drop(data.iloc[:, y-1:y],axis=1).values
        x_normalized = np.concatenate((np.ones([x_normalized.shape[0],1]),x_normalized),axis=1) # Add dummy x's
        # Define initial parameters
        m = len(data.index) # length of dataset
        return x_normalized, y_normalized, m

    def linReg(self, alpha, delta_j_threshold, regularize): # Multivariate regression
        X = self.X
        y = self.y
        m = self.m
        mvl_result = {} # Dictionary to hold final value arrays
        delta_j = 5
        j = []
        iteration = 1
        mvl_thetas = np.zeros([1,X.shape[1]])
        # Run the gradient descent  
        while iteration < 1000 and delta_j > delta_j_threshold:
            mvl_thetas = mvl_thetas - (alpha/m)*np.sum(X*(X @ mvl_thetas.T - y), axis=0)
            j.append(np.sum(np.power(((X @ mvl_thetas.T) - y),2))/(2*m))
            delta_j = j[iteration] - j[iteration-1]
            iteration+= 1
        mvl_result['j'] = j
        mvl_result["thetas"] = list(mvl_thetas)
            
        # Return the results of the mvl regression
        return mvl_result

    def logReg(self,alpha,delta_j_threshold,regularize): # Logistic Regression
        X = self.X
        y = self.y
        m = self.m
        mvl_result = {} # Dictionary to hold final value arrays
        delta_j = 5
        j = [5]
        iteration = 1
        mvl_thetas = np.zeros([1,X.shape[1]]) # Initialize theta matrix
        # Generate the matrix for regularizing the thetas
        if regularize != 0:
            l = [1 - alpha * (regularize/m)] * X.shape[1] # make list l with regularization terms
            l[0] = 1 # Set the first element to one because we don't regularize theta_0
            mvl_regTerms = np.asarray(l) # Create numpy array with regularization terms
        else:
            mvl_regTerms = np.ones([1,X.shape[1]]) # Set numpy array to ones if regularize = 0
        # Run the gradient descent  
        while delta_j > delta_j_threshold:
            h = 1/(1+np.exp(-(X @ mvl_thetas.T))) # Calculate h(x)     
            mvl_thetas = mvl_thetas * mvl_regTerms - (alpha/m)*np.sum(X*(h - y), axis=0) # Update theta matrix
            j.append( (-1/m)*np.sum((y * np.log(h))+(1 - y)*np.log(1-h)) + (regularize/(2*m))*np.sum(mvl_thetas ** 2)) # Update J(theta)
            delta_j = abs(j[iteration] - j[iteration-1]) # Update delta J
            iteration+= 1
        # Return the results of the regression
        mvl_result['j'] = j
        mvl_result["thetas"] = mvl_thetas
        return mvl_result
    
    def predict(self, data, y, thetas, threshold):
        X, y, m = self.__prepData(data,y,False) # Prep the input data (pandas)
        h = 1/(1+np.exp(-(np.dot(X,thetas.T)))) # calculate prediction
        return int(h >= threshold) # Return integer of T/F test h greater than or equal to threshold