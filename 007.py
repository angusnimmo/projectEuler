primes = [2]
check = 3

def isPrime(primes, n):
    for i in primes:
        if (n % i) == 0:
            return False
    return True
    
while len(primes) < 10001:
    if isPrime(primes, check):
        primes.append(check)
    check += 1
    
print(primes[-1])
