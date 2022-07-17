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

if __name__ == "__main__":
    nSize = 3
    primeCount = 0

    while True:
        # North east
        if isPrime((nSize-1)**2 - nSize + 2):
            primeCount += 1
            
        # South east, coprime by definition
        # if isPrime((nSize)**2):
            # primeCount += 1
            
        # South West
        if isPrime((nSize)**2 - nSize + 1):
            primeCount += 1
            
        # North west
        if isPrime((nSize-1)**2 + 1):
            primeCount += 1
        
        ratio = primeCount / (2*nSize - 1)
        
        if ratio < 0.1:
            break
        else:
            nSize += 2
            
    print(nSize)
