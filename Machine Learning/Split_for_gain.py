"""
Calculate Information Gain.

Task
Given a dataset and a split of the dataset, calculate the information gain using the gini impurity.

The first line of the input is a list of the target values in the initial dataset. The second line is the target values of the left split and the third line is the target values of the right split.

Round your result to 5 decimal places. You can use round(x, 5).

Input Format
Three lines of 1's and 0's separated by spaces

Output Format
Float (rounded to 5 decimal places)

Sample Input
1 0 1 0 1 0
1 1 1
0 0 0

Sample Output
0.5
"""
T = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]

def gini(x):
    p = sum(x)/len(x)
    return (2*p*(1-p))

out = gini(T) - gini(L)*len(L)/len(T) - gini(R)*len(R)/len(T)

print(round(out,5))