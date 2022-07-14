import sys
from fractions import Fraction

def continuedFraction(iteration):
    if iteration == 0:
        return Fraction(1, 2)
    else:
        return Fraction(1, 2 + continuedFraction(iteration - 1))
        
def rootTwoSeries(x):
    return 1 + continuedFraction(x)
    
def numLongerThanDenom(x):
    return len(str(x.numerator)) > len(str(x.denominator))
    
if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    print(len([i for i in range(1000) if numLongerThanDenom(rootTwoSeries(i))]))
