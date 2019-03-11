# Neural Network

# I used some of the clever coding tricks from this article:
# https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
# Some of the math is from this article:
# 
# There are still a couple of issues with it, but using LOA cross validation with the iris data set,
# I was able to achieve 95% prediction accuracy.
# One of the issues that I have seen is that it outputs 149 nodes even in the prediction method,
# All of the nodes end up being the same since there is only one input node, but this should be
# fixable. I don't have the time to fix it since I need to study for my oral qualifying exam.
import pandas as pd
import random
import numpy as np
import math
import sys
from scipy.stats import zscore

class NeuralNetwork():

    def __init__(self,data,y, normalize=False):
        self.X = data
        self.y = y
        self.m = len(data)
        self.layerList = []
        self.learningRate = 1
        self.thetas = []
        self.updateThetasList = []
        self.cost = 2
        self.output = np.zeros(self.y.shape)
        self.z_vecs = []
        self.a_vecs = []
        self.updateBiasList = []

    def __sigmoid(self,x):
        return 1. / (1. + np.exp(-x))
        #return x * (0.1* x > 0) # relu
    
    def __derivativeSigmoid(self,x):
        x = self.__sigmoid(x)
        return x * (1 - x)
        #return 1 * (x > 0) # relu

    def __fprop(self, layers, nodes): # Forward Propagation
        for l in range(0,layers+1):
            #print("b shape: {} ".format(self.biases[l].shape))
            #print("z shape: {}".format(np.dot(self.layerList[l],self.thetas[l]).shape))
            z_vec = np.dot(self.layerList[l],self.thetas[l]) + self.biases[l]
            self.z_vecs[l] = z_vec 
            a_vec = self.__sigmoid(z_vec)
            self.layerList[l+1] = a_vec

    def __bprop(self,layers): # Backward Propagation
        #print(self.y - self.layerList[-1])
        delta_L = (self.layerList[-1]-self.y) * self.__derivativeSigmoid(self.z_vecs[-1]) # Our prediction error
        self.updateBiasList[-1] = delta_L
        self.updateThetasList[-1] = self.layerList[-2].T @ delta_L
        #delta_L = ( delta_L @ self.thetas[-1].T) * self.__derivativeSigmoid(self.z_vecs[-2])
        for l in range(2,layers+2):
            if l == 1:
                self.updateThetasList[-l] = self.layerList[-l-1].T @ delta_L
            else:
                #z = np.dot(self.thetas[-l+1].transpose(), delta_L)
                try: 
                    delta_L = ( delta_L @ self.thetas[-l+1].transpose() ) * self.__derivativeSigmoid(self.z_vecs[-l])
                except AttributeError as e:
                    print(self.thetas[-l+1])
                    sys.exit(0)
                self.updateBiasList[-l] = delta_L
                self.updateThetasList[-l] = self.layerList[-l-1].T @ delta_L
        self.__updateThetas(layers)
 
    def __updateThetas(self,layers):
        #print(self.updateBiasList[0])
        for l in range(0,layers+1):
            #self.thetas[l] += self.updateThetasList[l]
            self.thetas[l] = np.array([w-(self.learningRate/len(self.X))*nw for w,nw in zip(self.thetas[l],self.updateThetasList[l])])
            self.biases[l] = np.array([b-(self.learningRate/len(self.X))*nb for b,nb in zip(self.biases[l],self.updateBiasList[l].flatten())])

    def __calcCost(self,thetas):
        #return (-1/self.m) * ((self.y * np.log(self.__sigmoid(thetas))) + (1 - self.y) * np.log(1 - self.__sigmoid(thetas)))
        return 0.5*np.sum((self.y-thetas)**2)

    def __initializeHiddenLayers(self,layers,nodesPerLayer,train):
        self.updateThetasList = [None] * (layers+1)
        self.z_vecs = [None] * (layers+1)
        self.updateBiasList = [None] * (layers+1)
        for l in range(0,layers+1):
            self.layerList.append(None)
        if train:
            for l in range(0,layers-1):
                self.biases.append(np.random.randn(nodesPerLayer))
            self.biases.append(np.random.randn(self.y.shape[1]))
            Innodes = nodesPerLayer
            Outnodes = Innodes
            for l in range(0,layers):
                if l == (layers-1):
                    Outnodes = self.y.shape[1]
                self.thetas.append(np.random.uniform(low=-1,high=1,size=(Innodes, Outnodes)))
            self.initThetas = self.thetas

    def train_model(self,hiddenLayers,nodesPerLayer): 
        self.layers = hiddenLayers
        self.nodesPerLayer = nodesPerLayer
        a_vec = self.X # Input layer
        self.biases = [np.random.randn(len(self.X), 1)]
        self.a_vecs.append(a_vec)
        self.layerList.append(a_vec)
        self.thetas.append(np.random.uniform(low=-1,high=1,size=(a_vec.shape[1], nodesPerLayer)))
        #Create the hidden layer framework
        self.__initializeHiddenLayers(layers=self.layers,nodesPerLayer=self.nodesPerLayer,train=True)
        iteration = 1
        delta_j = 1
        #Train the neural network
        while delta_j > 0.0001: # iteration < 10: #
            self.__fprop(hiddenLayers,nodesPerLayer)
            self.__bprop(hiddenLayers)
            cc = np.mean(self.__calcCost(self.layerList[-1]))
            delta_j = abs(self.cost - cc)
            self.cost = cc
            iteration += 1
        self.output = self.layerList[-1]
        self.layerList = []

    def predict(self, data, y):
        self.X = data
        self.y = y
        self.layerList.append(self.X)
        self.__initializeHiddenLayers(layers=self.layers,nodesPerLayer=self.nodesPerLayer,train=False)
        self.__fprop(layers=self.layers,nodes=self.nodesPerLayer)
        return self.layerList[-1]

if __name__ == "__main__":
    toyDS = pd.read_csv('/Users/atrautm1/Downloads/toy_data_for_LDA.csv')
    a = NeuralNetwork(toyDS,3,True)
    a.train_model(2,2)
    print(a.output)  
