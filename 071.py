boundNum = 3
boundDen = 7
bestNum = 2
bestDen = 5
limit = 10**6

for testDen in range(limit, 1, -1):
    testNum = int((boundNum * testDen - 1) / boundDen)
    
    if (testNum * bestDen > bestNum * testDen):
        bestNum = testNum
        bestDen = testDen
        
print(bestNum, bestDen)
