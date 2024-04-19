# For this problem we are interested in knowing the number of non-empty bins 
# remaining after  N balls are thrown at random into N bins as a function of N.
# For this assignment you are to write code to run a simulation for each value of N from 1 to 1000, 
from random import random, seed
# import numpy as np
seed(37) #Fav random seed

numBalls = []  # X axis
nonEmptyBins = [] # Y axis
# Run simulation
for N in range (1000):
    N += 1 # we want to start with 1 ball
    numBalls.append(N)

    # make a dictionary for the balls, N - size dict = empty
    bins = {}
    for i in range (N):
        ballNum = int(random() * N)
        if(ballNum not in bins):
            bins[ballNum] = 1
        else:
            bins[ballNum] += 1 #Dont really need this but good for making sure of cor data
    nonEmptyCount = len(bins)
    nonEmptyBins.append(nonEmptyCount)


# and plot the results using the matplotlib plot function.
# we have the number of empty bins but we need to plot it against num balls

# X = np.array(numBalls) #.reshape(-1, 1)
# Y = np.array(numEmptyBins)
import matplotlib.pyplot as plt # for graphing
plt.plot(numBalls, nonEmptyBins)
plt.show()


# We would like to know the slope of this linear relationship.
# Write code to run a linear regression to find the best fit line for your dataset. 
from scipy import stats

reg = stats.linregress(numBalls, nonEmptyBins)
print("slope: " + str(reg.slope))
print("intercept: " + str(reg.intercept))
print("rvalue: " + str(reg.rvalue))

# Your output should be similar to the following:
# SciPy Linear Regression Solution 
#  slope:  0.6325801874018306
#  intercept: -0.02602000798390236        
#  rvalue: 0.997749733854947