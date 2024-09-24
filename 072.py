from datetime import datetime
from math import gcd


def main():
    start_time = datetime.now()
    n = int(1e6)
    mu = sieve_mobius(n)
    count = 3
    
    for i in range(1, n + 1):
        count += mu[i] * ((n // i) ** 2)
    
    print((count // 2) - 2) # Not including 0/1 and 1/1
    print(datetime.now() - start_time)
    
    
def sieve_mobius(limit: int) -> list[int]:
    mobius = [1] * (limit + 1)
    
    for i in range(2, int(limit ** .5) + 1):
        if mobius[i] == 1:
            for j in range(i, limit + 1, i):
                mobius[j] *= -i
            
            for j in range(i ** 2, limit + 1, i ** 2):
                mobius[j] = 0
                
    for i in range(2, limit + 1):
        if mobius[i] == i:
            mobius[i] = 1
        elif mobius[i] == -i:
            mobius[i] = -1
        elif mobius[i] < 0:
            mobius[i] = 1
        elif mobius[i] > 0:
            mobius[i] = -1
            
    return mobius



if __name__ == '__main__':
    main()
