from math import sqrt

def pent(n):
    return int(n*((3*n)-1)/2)
    
def checkPent(x):
    return (sqrt(1+24*x)%6 == 5)
    
def condition(i, j):
    return (checkPent(pent(i)+pent(j)) and checkPent(pent(i)-pent(j)))
    
flag = True
i = 2

while flag:
    iPent = pent(i)
    
    for j in range(i-1, 0, -1):
        jPent = pent(j)
        
        if (checkPent(iPent + jPent) and checkPent(iPent - jPent)):
            print(iPent - jPent)
            flag = False
            break
            
    i += 1
