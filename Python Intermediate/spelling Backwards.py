"""
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
"""
def spell(txt):
    if len(txt) == 1:
        print(txt)
    else:
        spell(txt[1:])
        print(txt[0])

txt = input()
spell(txt)