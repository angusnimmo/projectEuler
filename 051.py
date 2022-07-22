import itertools

def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(limit**0.5)+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return primeArray
    
def digitReplacements(n, primeArray):
    nStr = str(n)
    nDig = len(nStr)
    maxPrimes = 0
    rootPrime = 0
    
    for i in range(1, nDig):
        indices = [list(j) for j in itertools.combinations(range(nDig), i)]
        
        for j in indices:
            nList = list(nStr)
            primeFamily = []
            
            for l in range(10):
                for k in j:
                    nList[k] = str(l)

                # Conditional for leading zeros
                if nList[0] != '0':
                    test = int(''.join(nList))
                    
                    if primeArray[test]:
                        primeFamily.append(test)
                    
            if len(primeFamily) > maxPrimes:
                maxPrimes = len(primeFamily)
                rootPrime = min(primeFamily)
                
    return (rootPrime, maxPrimes)
    
if __name__ == "__main__":
    flag = True
    order = 2
    
    while flag:
        limit = 10**order
        primeArray = sievePrimes(10**order)
        
        for i in range(10**(order-2), 10**(order-1)):
            if primeArray[i]:
                root = digitReplacements(i, primeArray)
                
                if root[1] >= 8:
                    print(root[0])
                    flag = False
                    break
                    
        order += 1
