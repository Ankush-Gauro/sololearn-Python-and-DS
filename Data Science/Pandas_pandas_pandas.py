"""
Finding the next centroid

Unsupervised learning algorithm clustering involves updating the centroid of each cluster. Here we find the next centroids for given data points and initial centroids.

Task
Assume that there are two clusters among the given two-dimensional data points and two random points (0, 0), and (2, 2) are the initial cluster centroids. Calculate the euclidean distance between each data point and each of the centroid, assign each data point to its nearest centroid, then calculate the new centroid. If there's a tie, assign the data point to the cluster with centroid (0, 0). If none of the data points were assigned to the given centroid, return None.
 
Input Format 
First line: an integer to indicate the number of data points (n)
Next n lines: two numeric values per each line to represent a data point in two dimensional space.

Output Format
Two lists for two centroids. Numbers are rounded to the second decimal place.

Sample Input 
3
1 0
0 .5
4 0

Sample Output 
[0.5  0.25]
[4. 0.]
"""
import numpy as np

n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
    
X = np.array(X)
X1 = np.array([0, 0])
X2 = np.array([2, 2])

a = []
b = []

for i in range(n):
    if np.sqrt(((X[i] - X1)**2).sum()) <= np.sqrt(((X[i] - X2)**2).sum()):
        a.append(X[i])
    elif np.sqrt(((X[i] - X1)**2).sum()) > np.sqrt(((X[i] - X2)**2).sum()):
        b.append(X[i])

a = np.array(a)
b = np.array(b)

sum_a1 = 0
sum_a2 = 0
sum_b1 = 0
sum_b2 = 0

for i in range(len(a)):
    sum_a1 += a[i][0]
    sum_a2 += a[i][1]
    
for i in range(len(b)):
    sum_b1 += b[i][0]
    sum_b2 += b[i][1]

if len(a != 0):
    sum_a1 /= len(a)
    sum_a2 /= len(a)
    sum_a1 = sum_a1.round(2)
    sum_a2 = sum_a2.round(2)
    
if len(b != 0):
    sum_b1 /= len(b)
    sum_b2 /= len(b)
    sum_b1 = sum_b1.round(2)
    sum_b2 = sum_b2.round(2)
    
c = []
c.append(sum_a1)
c.append(sum_a2)
d = []
d.append(sum_b1)
d.append(sum_b2)

if len(a) == 0:
    print(None)
else:
    print(c)

if len(b) == 0:
    print(None)
else:
    print(d)
    

