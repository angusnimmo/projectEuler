import math

def choose(n, r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
    
solutions = [choose(i, j) for i in range(101) for j in range(i+1) if choose(i, j) > 1000000]

print(len(solutions))
