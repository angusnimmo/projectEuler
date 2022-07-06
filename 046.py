from math import sqrt
    
def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(sqrt(limit))+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, primeCheck) in enumerate(primeArray) if primeCheck]

def calc(magnitude):
    primes = sievePrimes(magnitude)
    oddComposites = list(set(range(9, magnitude, 2)) - set(primes))
    doubleSquares = [2*(i**2) for i in range(1, int(sqrt(oddComposites[-1]/2))+1)]
    boolArray = [True] * magnitude

    for i in oddComposites:
        boolArray[i] = False


    for i in primes:
        for j in doubleSquares:
            if i+j >= magnitude:
                break
            else:
                boolArray[i+j] = True
                
    return boolArray
    
if __name__ == "__main__":
    order = 10
    result = calc(order)
    
    while all(result):
        order *= 10
        result = calc(order)
        
    print([i for (i, x) in enumerate(result) if not x])
