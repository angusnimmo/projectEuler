from datetime import datetime
from itertools import combinations


def main():
    start_time = datetime.now()
    limit = 1e7
    primes = sieve_primes(int(1e3), int(1e4))
    minimum = float('inf')
    result = 0
    
    for p1, p2 in combinations(primes, 2):
        n = p1 * p2
        
        if n <= limit:
            totient = (p1 - 1) * (p2 - 1)
            
            if is_permutation(n, totient):
                temp = n / totient
                
                if temp < minimum:
                    minimum = temp
                    result = n
                    
    print(result)
    print(datetime.now() - start_time)
    
    
def sieve_primes(lower: int, upper: int) -> list[int]:
    prime_array = [True] * upper
    prime_array[0] = prime_array[1] = False
    
    for (i, prime) in enumerate(prime_array[: int(upper ** .5) + 1]):
        if prime:
            for j in range(i ** 2, upper, i):
                prime_array[j] = False
                
    return [i for (i, prime) in enumerate(prime_array) if prime and i >= lower]


def is_permutation(a: int, b: int) -> bool:
    A = [int(x) for x in str(a)]
    B = [int(x) for x in str(b)]
    count = [0 for _ in range(10)]
    
    if len(A) != len(B):
        return False
    else:
        for i in range(len(A)):
            count[A[i]] += 1
            count[B[i]] -= 1
            
    return all(x == 0 for x in count)


if __name__ == '__main__':
    main()
