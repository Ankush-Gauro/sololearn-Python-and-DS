"""
Calculating Evaluation Metrics using the Confusion Matrix.

Task
You will be given the values of the confusion matrix (true positives, false positives, false negatives, and true negatives). Your job is to compute the accuracy, precision, recall and f1 score and print the values rounded to 4 decimal places. To round, you can use round(x, 4).

Input Format
The values of tp, fp, fn, tn, in that order separated by spaces

Output Format
Each value on its own line, rounded to 4 decimal places, in this order:
accuracy, precision, recall, f1 score

Sample Input
233 65 109 480

Sample Output
0.8038
0.7819
0.6813
0.7281
"""
tp, fp, fn, tn = [int(x) for x in input().split()]
accuracy = ((tp + tn) / (tp +fp+fn+tn))
precision = (tp / (tp + fp))
recall = (tp / (tp + fn))
F1_score = (2 * precision * recall / (precision + recall))
print(round(accuracy, 4))
print(round(precision, 4))
print(round(recall,4))
print(round(F1_score,4))