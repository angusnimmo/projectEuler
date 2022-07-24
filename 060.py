import networkx as nx
from itertools import combinations

def isPrime(n):
    if (n == 0) or (n == 1): 
        return False 
    if n == 2: 
        return True 
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0: 
            return False 
    return True
    
def sievePrimes(limit):
    primeArray = [True] * limit
    primeArray[0] = primeArray[1] = False
    
    for (i, primeCheck) in enumerate(primeArray[:int(limit**0.5)+1]):
        if primeCheck:
            for j in range(i**2, limit, i):
                primeArray[j] = False
                
    return [i for (i, isPrime) in enumerate(primeArray) if isPrime]
    
def isPrimeConcat(a, b):
    return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))

if __name__ == "__main__":
    vertices = sievePrimes(10000)
    vertices.remove(2)
    vertices.remove(5)
    edges = [i for i in combinations(vertices, 2) if isPrimeConcat(i[0], i[1])]
    primeGraph = nx.Graph()
    primeGraph.add_edges_from(edges)
    primeCliques = list(nx.find_cliques(primeGraph))
    cliqueSums = [sum(i) for i in primeCliques if len(i) == 5]
    print(cliqueSums)
