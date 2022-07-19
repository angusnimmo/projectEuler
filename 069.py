def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(limit**0.5)+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, primeCheck) in enumerate(primeArray) if primeCheck]

def primeFactors(n):
    pf = []
    
    while (n % 2 == 0):
        pf.append(2)
        n /= 2
        
    for i in range(3, int(n**0.5)+1, 2):
        while (n % i == 0):
            pf.append(i)
            n /= i
            
    if n > 2:
        pf.append(int(n))
        
    return set(pf)
    
def totientPrimeFactors(n):
    pf = primeFactors(n)
    result = n
    
    for i in pf:
        result *= (1 - (1/i))
        
    return int(result)
    
if __name__ == "__main__":
    limit = 1000000
    primes = sievePrimes(limit)
    result = 1
    primeIndex = 0
    
    while (result <= limit):
        result *= primes[primeIndex]
        primeIndex += 1

    result = int(result / primes[primeIndex-1])
    print(result)
