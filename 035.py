from math import sqrt

def seivePrimes(pMax):
    x = list(range(2, pMax))
    y = list(range(2, int(sqrt(pMax))))
    composites = []

    for i in y:
        for j in range(i**2, pMax, i):
            composites.append(j)
        
    primes = list(set(x) - set(composites))
    primes.sort()
    
    return primes
    
primes = seivePrimes(1000000)
nonCircularPrimes = []

for i in primes[5:]:
    for j in str(i):
        if int(j) % 2 == 0:
            nonCircularPrimes.append(i)

primes = list(set(primes) - set(nonCircularPrimes))
primes.sort()

for i in primes[5:]:
    pLen = len(str(i))
    primeCycles = [''.join([str(i)[(j+k) % pLen] for j in range(pLen)]) for k in range(pLen)]
    
    for j in primeCycles:
        if (int(j) not in primes):
            nonCircularPrimes.append(i)
            
primes = list(set(primes) - set(nonCircularPrimes))
primes.sort()

print(len(primes))
