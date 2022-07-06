import numpy as np
from math import sqrt

def isPrime(n): 
    if (n == 0) or (n == 1): 
        return False 
    if n == 2: 
        return True 
    for i in range(2, int(sqrt(n))+1): 
        if n % i == 0: 
            return False 
    return True

def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(sqrt(limit))+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, primeCheck) in enumerate(primeArray) if primeCheck]

limit = 1000000
primes = sievePrimes(limit)
primesCumsum = list(np.cumsum(primes))

prime = 0
primeIndex = 0

for i in range(len(primesCumsum)):
    for j in range(i + primeIndex, len(primesCumsum)):
        checkSum = primesCumsum[j] - primesCumsum[i]
        
        if checkSum >= limit:
            break
        
        if isPrime(checkSum):
            prime = checkSum
            primeIndex = j-i  
        
print(prime)
