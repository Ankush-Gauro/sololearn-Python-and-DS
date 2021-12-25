"""
In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]
"""
n, p = [int(x) for x in input().split()]
import numpy as np
a = np.empty((0,p), float)
for i in range(n):
    a = np.append(a, np.array([input().split()]).astype(float), axis = 0)

print(a.mean(axis =1).round(2))