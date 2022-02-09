"""
Build a Random Forest model.

Task
You will be given a feature matrix X and target array y. Your task is to split the data into training and test sets, build a Random Forest model with the training set, and make predictions for the test set. Give the random forest 5 trees.

You will be given an integer to be used as the random state. Make sure to use it in both the train test split and the Random Forest model.

Input Format
First line: integer (random state to use)
Second line: integer (number of datapoints)
Next n lines: Values of the row in the feature matrix, separated by spaces
Last line: Target values separated by spaces

Output Format
Numpy array of 1's and 0's

Sample Input
1
10
-1.53 -2.86
-4.42 0.71
-1.55 1.04
-0.6 -2.01
-3.43 1.5
1.45 -1.15
-1.6 -1.52
0.79 0.55
1.37 -0.23
1.23 1.72
0 1 1 0 1 0 0 1 0 1

Sample Output
[1 0 0]
"""
import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

random_state = int(input())
n = int(input())
rows = []
for i in range(n):
    rows.append([float(a) for a in input().split()])

X = np.array(rows)
y = np.array([int(a) for a in input().split()])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = random_state)
rf = RandomForestClassifier(n_estimators=5,random_state=random_state)
rf.fit(X_train ,y_train)
print(rf.predict(X_test))