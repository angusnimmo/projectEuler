import numpy as np
from fractions import Fraction

curiousNums = []
curiousDenoms = []

def falseSimplify(num, denom):
    numStr = str(num)
    denomStr = str(denom)
    
    if (num % 10 == 0) or (denom % 10 == 0):
        return  False
    else:
        if (numStr[0] == denomStr[0]) and (int(numStr[1]) / int(denomStr[1]) == num / denom):
            return True
        if (numStr[1] == denomStr[0]) and (int(numStr[0]) / int(denomStr[1]) == num / denom):
            return True
        if (numStr[0] == denomStr[1]) and (int(numStr[1]) / int(denomStr[0]) == num / denom):
            return True
        if (numStr[1] == denomStr[1]) and (int(numStr[0]) / int(denomStr[0]) == num / denom):
            return True
        return False
    return False

for i in range(11, 99):
    for j in range(i+1, 100):
        if falseSimplify(i, j):
            curiousNums.append(i)
            curiousDenoms.append(j)
            
print(Fraction(np.prod(curiousNums), np.prod(curiousDenoms)))
