import itertools
from math import sqrt

nSize = 1001
current = (0, 0)
coordinates = {}

def R(coordinate):
    return [coordinate[0]+1, coordinate[1]]

def D(coordinate):
    return [coordinate[0], coordinate[1]-1]

def L(coordinate):
    return [coordinate[0]-1, coordinate[1]]

def U(coordinate):
    return [coordinate[0], coordinate[1]+1]

moveMagnitude = list(range(1, nSize))
moveMagnitude = [[i]*2 for i in moveMagnitude]
moveMagnitude = list(itertools.chain.from_iterable(moveMagnitude))
moveMagnitude.append(moveMagnitude[-1])

moveCycle = [R, D, L, U]

while len(moveCycle) < 2*nSize - 1:
    moveCycle.extend(moveCycle)

moveCycle = moveCycle[:2*nSize -1]
moveCycle = [[moveCycle[i]]*moveMagnitude[i] for i in range(2*nSize - 1)]
moveCycle = list(itertools.chain.from_iterable(moveCycle))
moveCycle.append(moveCycle[-1])

for i in range(nSize**2):
    coordinates[current] = i + 1
    current = tuple(moveCycle[i](list(current)))

mainDiagonal = [(i, -i) for i in range(-(nSize//2), nSize//2 + 1)]
antiDiagonal = [(i, i) for i in range(-(nSize//2), nSize//2 + 1)]
diagonals = list(set(mainDiagonal + antiDiagonal))

print(sum([coordinates[i] for i in diagonals]))
