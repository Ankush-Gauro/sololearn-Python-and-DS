"""
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""
a = input().split() #splits it into a string
lengths = []

for i in a:
   lengths.append(len(i))
#len
x=max(lengths) #max
y=lengths.index(x) #indexing in a
print(a[y])