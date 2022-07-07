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
    
primes = sievePrimes(18)

def condition(pandigital):
    return all([int(pandigital[i+1:i+4]) % primes[i] == 0 for i in range(7)])
    
solution = sum([int(''.join(i)) for i in itertools.permutations('0123456789') if condition(''.join(i))])

print(solution)
