from datetime import datetime


def main():
    start_time = datetime.now()
    n = 100
    primes = sieve_primes(2, n)
    ways = [0] * (n + 1)
    ways[0] += 1
    
    for p in primes:
        for i in range(p, n + 1):
            ways[i] += ways[i - p]
            
    print(next(i for i, x in enumerate(ways) if x > 5000))
    print(datetime.now() - start_time)
    
    
def sieve_primes(lower: int, upper: int) -> list[int]:
    prime_array = [True] * upper
    prime_array[0] = prime_array[1] = False
    
    for (i, prime) in enumerate(prime_array[: int(upper ** .5) + 1]):
        if prime:
            for j in range(i ** 2, upper, i):
                prime_array[j] = False
                
    return [i for i, x in enumerate(prime_array) if x]
    
    
    
if __name__ == '__main__':
    main()
