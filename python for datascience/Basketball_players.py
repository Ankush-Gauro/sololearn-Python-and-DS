"""
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.
"""
def mean(array): 
    x=0
    for j in array:
        x+=j
    return x/len(array)
    
def std(a):  
    sum=0
    for j in a:
        sum+=j**2
    y = abs(mean(a)**2 - sum/len(a))
    return y**0.5

def rstd(a): 
    ans=0
    m = mean(a)
    st = std(a)
    for x in players:
        if (m-st) <= x <= (m+st):
            ans+=1
    return ans
    
    
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
print(rstd(players))