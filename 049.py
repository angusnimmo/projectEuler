import itertools
from math import sqrt

def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(sqrt(limit))+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, primeCheck) in enumerate(primeArray) if primeCheck]
    
# Take in prime permutations, return sequences that are solutions
def sequenceCheck(pp):
    sequencesOfThree = [sorted(i) for i in itertools.combinations(pp, 3)]
    
    for i in sequencesOfThree:
        if (i[2] - i[1]) == (i[1] - i[0]):
            return i
    
primes = sievePrimes(10000)
primes = [i for i in primes if i > 1000]
primesDigits = sorted(list(set([''.join(sorted(str(i))) for i in primes])))
primesDigitsDict = {}

for i in primes:
    sortedPrime = ''.join(sorted(str(i)))
    
    if sortedPrime in primesDigitsDict:
        primesDigitsDict[sortedPrime].append(i)
    
    elif sortedPrime not in primesDigitsDict:
        primesDigitsDict[sortedPrime] = [i]
        
possibleSolutions = [i for i in list(primesDigitsDict.values()) if len(i) >= 3]
solutionSequences = [sequenceCheck(i) for i in possibleSolutions if sequenceCheck(i) != None]
solutions = [''.join([str(j) for j in i]) for i in solutionSequences]

print(solutions)
