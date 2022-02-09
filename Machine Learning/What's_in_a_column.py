"""
Getting a column from a numpy array.

Task
Given a csv file and a column name, print the elements in the given column.

Input Format
First line: filename of a csv file
Second line: column name

Output Format
Numpy array

Sample Input
https://sololearn.com/uploads/files/one.csv
a

File one.csv contents:
a,b
1,3
2,4

Sample Output
[1 2]
"""
import numpy as np
import pandas as pd

filename = input()
column_name = input()

df1 = pd.read_csv(filename)


print(np.array(df1[column_name]))