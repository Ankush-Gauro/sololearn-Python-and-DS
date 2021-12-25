"""
Ordinary least squares for linear regression.

Ordinary least squares (OLS) is a method to estimate the parameters β in a simple linear regression, Xβ = y, where X is the feature matrix and y is the dependent variable (or target), by minimizing the sum of the squares of the differences between the observed dependent variable in the given dataset and those predicted by the linear function. Mathematically, the solution is given by the formula in the image, where the superscript T means the transpose of a matrix, and the superscript -1 means it is an inverse of a matrix.

Task
Given a 2D array feature matrix X and a vector y, return the coefficient vector; see the formula.

Input Format
First line: two integers separated by spaces, the first indicates the rows of the feature matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in the feature matrix
Last line: p values of target y

Output Format
An numpy 1d array of values rounded to the second decimal.

Sample Input
2 2
1 0
0 2
2 3

Sample Output
[2. , 1.5]
"""
import numpy as np
n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]

X=np.array(X)
xt=X.T
x=xt.dot(X)
xinv=np.linalg.inv(x)
a=np.matmul(xt,y)
a=np.matmul(a,xinv)
a=np.round(a,2)
print(a)