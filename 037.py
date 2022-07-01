from math import sqrt

primeOrder = 1

def isPrime(n): 
    if (n == 0) or (n == 1): 
        return False 
    if n == 2: 
        return True 
    for i in range(2, int(sqrt(n))+1): 
        if n % i == 0: 
            return False 
    return True 

def isTwoSidedPrime(p):
    primeString = str(p)
    for i in range(1, len(primeString)):
        if (not isPrime(int(primeString[i:]))) or (not isPrime(int(primeString[:i]))) :
            return False
    return True

def sieveTwoSidedPrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(sqrt(limit))+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, primeCheck) in enumerate(primeArray) if primeCheck and isTwoSidedPrime(i)][4:]
   
solutions = sieveTwoSidedPrimes(10**primeOrder)

while len(solutions) < 11:
    primeOrder += 1
    solutions = sieveTwoSidedPrimes(10**primeOrder)
    
print(sum(solutions))
