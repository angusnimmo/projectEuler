import math
import itertools

x = list(range(2, 2000))
y = list(range(2, int(math.sqrt(2000))))
nonPrimes = []

for i in y:
    for j in range(i**2, 2000, i):
        nonPrimes.append(j)
        
primes2000 = sorted(set(x) - set(nonPrimes))

# Condition set by n = 0 (b must be prime and <= 1000)
bList = primes2000[:168]

# Condition set by n = 1
aList = [i[0]-1-i[1] for i in itertools.product(primes2000, bList)]

# Remove duplicates from aList and sort
aList = list(dict.fromkeys(aList))
aList = sorted(aList)

abDict = {}

def isPrime(p):
    if p <= 1:
        return False
    
    for i in range(2, p):
        if (p % i) == 0:
            return False
    return True

def quadratic(n, a, b):
    return (n**2 + a*n + b)

for b in bList:
    # Condition set by smallest prime, 2
    aListSlice = aList[aList.index(1-b):]
    
    for a in aListSlice:
        n = 0
        consecutivePrimes = 0
        
        while isPrime(quadratic(n, a, b)):
            consecutivePrimes += 1
            n += 1
            
        abDict[(a, b)] = n

maxKey = max(abDict, key=abDict.get)
maxValue = abDict[maxKey]

print(maxKey, maxValue)
