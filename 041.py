import itertools
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
    digits = '123456789'
    solutions = []
    
    for i in range(9, 0, -1):
        solutions.append([int(''.join(j)) for j in list(itertools.permutations(digits[:i])) if isPrime(int(''.join(j)))])
        solutions = list(itertools.chain.from_iterable(solutions))
        
        if len(solutions) > 0:
            break
    
    print(solutions[-1])
