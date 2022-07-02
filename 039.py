from math import sqrt

def greatestCommonDenominator(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    
def isCoprime(x, y):
    return greatestCommonDenominator(x, y) == 1

def bothOdd(x, y):
    if (x % 2 == 1) and (y % 2 == 1):
        return True
    return False

perimeters = [2*m*(m+n)*k for m in range(2, int(sqrt(500))) for n in range(m-1, 0, -1) for k in range(1, int(500/(m*(m+n)))+1) if (not bothOdd(m, n)) and isCoprime(m, n)]

print(max(set(perimeters), key=perimeters.count))
