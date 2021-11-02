"""
Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

Given an expression as input, we need to find out whether the parentheses are balanced or not.
For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.

The problem can be solved using a stack. 
Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered. 
If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced. 

Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not. 

Sample Input:
(a( ) eee) )

Sample Output:
False
"""






from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
        
    def size(self):
        return len(self.container)
        
def is_match(ch1, ch2):
    match_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
            
    return stack.size()==0

print(is_balanced(input()))
