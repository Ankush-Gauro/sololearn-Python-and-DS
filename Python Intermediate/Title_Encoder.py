"""
You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions, each on a new line.
"""
file = open("/usercode/files/books.txt", "r")
var = file.readlines()
for title in var:
    l = title.split(' ')
    s = ""
    for i in l:
        s += i[0]
    print(s)


file.close()