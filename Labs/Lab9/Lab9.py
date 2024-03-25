# Data from n estimators
# ESTIMATORS    CORRECT %
# 10            78.688%
# 20            81.967%
# 30            78.688% 
# 40            80.327%
# 50            80.327%
# 60            78.688%
# 70            80.327%
# 80            80.327%
# 90            81.967%

# No very strong correlation between num estimators and percentage
# I think that it is slightly getting higher specifically the end is promising
# However it looks like there is not that many samples as some scores were the exact same


#inlcudes for math and sklearn
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier # For forest assignment
from sklearn.model_selection import train_test_split

# ML Magic below very cool.
# I believe this is formatting the csv file
heart_disease = pd.read_csv('heart.csv')
X = heart_disease.drop(['target'] , axis=1) 
Y = heart_disease['target']

# Forest classifies and get train(what module gets info form) and test(what module attempts itself) vars
clf = RandomForestClassifier(n_estimators=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)                                                
# clf.fit(X_train, Y_train)
# y_pred = clf.predict(X_test)

# print(clf.score(X_train, Y_train))
# print(clf.score(X_test, Y_test))

# Start of experiments below!
np.random.seed(17) # Not sure if i want this is but youtube dude did.
# Not sure if moduel sayd to do from 1-10 or 10-100 estimators but experiment seems more valid with to 100
for i in range(10, 100, 10):
    print("Trying model with " + str(i) + " estimators")
    clf = RandomForestClassifier(n_estimators=i).fit(X_train, Y_train) # Use estimator param and fit the data
    print("Accuracy with " + str (i) + " estimators :" + str(clf.score(X_test, Y_test)))


# First outputs
# 0.9008264462809917
# 0.5573770491803278 (Super bad!)