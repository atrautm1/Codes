#!/usr/local/anaconda3/bin/python
# Aaron Trautman
# Qualifying Exam
# Machine Learning - UNC Charlotte, 2018
import numpy as np
import pandas as pd
from NeuralNetwork import NeuralNetwork
from sklearn.datasets import load_iris
import sys


wd = "/Users/atrautm1/Desktop/quals/Q4A/"

iris = load_iris() # Load the dataset

#ii = (iris.target) # Grab the samples # pylint: disable=no-member

my_X = iris.data[:, 2:4] # Set the X variables # pylint: disable=no-member
my_Y = iris.target # Set the Y values # pylint: disable=no-member

#Normalize
m = np.mean(my_X, axis=0)
sd = np.std(my_X, axis=0)

my_X[:,0] = (my_X[:,0] - m[0])/sd[0] 
my_X[:,1] = (my_X[:,1] - m[1])/sd[1] 

my_y = np.zeros((len(my_Y),3))
my_y[np.where(my_Y == 0),0] = 1.
my_y[np.where(my_Y == 1),1] = 1.
my_y[np.where(my_Y == 2),2] = 1.

costs = []
correctPrds = 0 
wrongPrds = 0
for i in range(0,len(my_X)):
    # Leave one out cross validation
    X_test = my_X[i,:]
    y_test = my_y[i,:]
    flowerType = my_Y[i]
    X = np.delete(my_X, i, axis=0)
    y = np.delete(my_y, i, axis=0)

    # Initialize the Network and train the model
    nn = NeuralNetwork(data=X, y=y)
    nn.train_model(hiddenLayers=3, nodesPerLayer=10)
    #print("The cost was: {}".format(nn.cost))
    costs.append(nn.cost)
    pred = nn.predict(data=X_test,y=y_test)
    pred = np.round(pred[0])
    try:
        p = True if pred[flowerType] == 1 else False
    except IndexError as e:
        print(pred)
        print(flowerType)
        sys.exit(0)
    if p:
        correctPrds += 1
    else:
        wrongPrds += 1
    if (i+1) % 15 == 0:
        n = np.round((((i+1)/150)*100))
        print("Done with {}%".format(n))



print("The average cost was {} with a standard deviation of {}.".format(np.mean(costs),np.std(costs)))
print("{} correct predictions and {} wrong predictions".format(correctPrds,wrongPrds))
