from math import sqrt

n = 2000000
x = list(range(2, n))
y = list(range(2, int(sqrt(n)) + 2))

nonPrimes = []

for i in y:
    for j in range(i**2, n, i):
        nonPrimes.append(j)
    
print(sum(set(x) - set(nonPrimes)))
