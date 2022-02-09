"""
Calculate Node Output.

Task
You are given the values for w1, w2, b, x1 and x2 and you must compute the output for the node. Use the sigmoid as the activation function.

Input Format
w1, w2, b, x1 and x2 on one line separated by spaces

Output Format
Float rounded to 4 decimal places

Sample Input
0 1 2 1 2

Sample Output
0.9820
"""
import math

w1, w2, b, x1, x2 = [float(x) for x in input().split()]
f = ((w1*x1) + (w2*x2) +b)

def sigmoid(x):
    return 1/(1+math.exp(-x))

sig = sigmoid(f)
sig = round(sig, 4)
print(sig)