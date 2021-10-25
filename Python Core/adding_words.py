"""
You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
"""
def concatenate(*args):
    words=args
    length=len(words)
    result=""
    inloop=0
    lastword=length-1
    while inloop<length:
        temp=words[inloop]
        if inloop is lastword:
            result+=temp
        else:
            result+=(temp+"-")
            
        inloop+=1
    return result

print(concatenate("I", "love", "Python", "!"))