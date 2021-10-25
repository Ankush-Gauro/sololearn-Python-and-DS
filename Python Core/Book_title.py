"""
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.
 
For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12
"""
file = open("/usercode/files/books.txt", "r")
x = file.readlines()
y = len(x)
for i in range(y):
    a=x[i][0] #it gets the first letter of the word at index i inthelist
    b = len(x[i])
    if i == y-1:
       print(a + str(b))
    else:
       print(a+ str(b-1))
file.close()