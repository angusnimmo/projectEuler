import itertools
import networkx as nx

def polygonal(V, n):
    return int((n/2)*((V-2)*n-(V-4)))
    
def polygonalLimit(V, limit):
    n = 1
    while polygonal(V, n) < limit:
        n += 1
    return n
    
def allPolygonals(xList):
    return all([any([i in j for i in xList]) for j in polygonals])

if __name__ == "__main__":
    polygonals = [[polygonal(i,j) for j in range(polygonalLimit(i, 1000), polygonalLimit(i, 10000))] for i in range(3, 9)]
    polygonalSet = set([i for j in polygonals for i in j])
    polygonalDict = {i: tuple(j for j in range(6) if i in polygonals[j]) for i in polygonalSet}
    potentialResults = []

    for i1 in polygonalSet:
        set2 = [i for i in polygonalSet if str(i1)[-2:] == str(i)[:2]]
        
        for i2 in set2:
            set3 = [i for i in polygonalSet if str(i2)[-2:] == str(i)[:2]]
            
            for i3 in set3:
                set4 = [i for i in polygonalSet if str(i3)[-2:] == str(i)[:2]]
                
                for i4 in set4:
                    set5 = [i for i in polygonalSet if str(i4)[-2:] == str(i)[:2]]
                    
                    for i5 in set5:
                         set6 = [i for i in polygonalSet if str(i5)[-2:] == str(i)[:2]]
                         
                         for i6 in set6:
                            if str(i6)[-2:] == str(i1)[:2]:
                                potentialResult = [i1, i2, i3, i4, i5, i6]
                                
                                if all([any([i in j for i in potentialResult]) for j in polygonals]):
                                    potentialResults.append(potentialResult)
                                
    potentialResults = list(set([tuple(sorted(i)) for i in potentialResults]))
    testType = [tuple(polygonalDict[i] for i in j) for j in potentialResults]
    solutionType = [i for i in testType if len(set(i)) == 6]
    solutionType = solutionType[0]
    print(sum(potentialResults[testType.index(solutionType)]))
