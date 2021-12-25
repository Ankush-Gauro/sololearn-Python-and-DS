"""
Confusion matrix of binary classification.

For binary classifications, a confusion matrix is a two-by-two matrix to visualize the performance of an algorithm. Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class.

Task
Given two lists of 1s and 0s (1 represents the true label, and 0 represents the false false) of the same length, output a 2darrary of counts, each cell is defined as follows

Top left: Predicted true and actually true (True positive)
Top right: Predicted true but actually false (False positive)
Bottom left: Predicted false but actually true (False negative)
Bottom right: Predicted false and actually false (True negative)

Input Format
First line: a list of 1s and 0s, separated by space. They are the actual binary labels. 
Second line: a list of 1s and 0s, the length is the same as the first line. They represented the predicted labels.

Output Format
A numpy 2darray of two rows and two columns, the first row contains counts of true positives and false positives and the second row contains counts of false negatives and true negatives.

Sample Input
1 1 0 0
1 0 0 0

Sample Output
[[1., 0.],
 [1., 2.]]
 """
 import numpy as np

y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

y_true = np.array(y_true)
y_pred = np.array(y_pred)

long = len(y_true)
tp = 0
fp = 0
fn = 0
tn = 0

for i in range(long):
    if y_pred[i] == 1:
        if y_true[i] == 1:
            tp += 1
            continue
        fp += 1
        continue
    if y_true[i] == 1:
        fn += 1
        continue
    tn += 1

result = np.array([tp, fp, fn, tn], dtype = 'f')
result = result.reshape((2, 2))
print(result)