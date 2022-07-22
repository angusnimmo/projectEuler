import requests

example = [[131, 673, 234, 103, 18],
           [201, 96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524, 37, 331]]               

def makeGraph(grid):
    nSize = len(grid)
    graph = {}
    
    for i in range(nSize):
        for j in range(nSize):
            graph[(i,j)] = {}
            
            if i+1 < nSize:
                graph[(i,j)][(i+1,j)] = grid[i+1][j]
                
            if j+1 < nSize:
                graph[(i,j)][(i,j+1)] = grid[i][j+1]
                
    return graph            
        
def bellmanFord(graph):
    distance = {}
    predecessor = {}
    vertices = set(i for i in graph.keys())
    
    for vertex in vertices:
        distance[vertex] = float('inf')
        predecessor[vertex] = None
        
    distance[(0,0)] = 0
    
    for _ in range(len(vertices)-1):
        for head in graph.keys():
            for (tail, weight) in graph[head].items():
                if (distance[head] + weight < distance[tail]):
                    distance[tail] = distance[head] + weight
                    predecessor[tail] = head
        
    return distance

if __name__ == "__main__":
    matrix = requests.get('https://projecteuler.net/project/resources/p081_matrix.txt').text
    matrix = matrix.split('\n')
    matrix = matrix[:-1]
    matrix = [[int(j) for j in i.split(',')] for i in matrix]
    matrixGraph = makeGraph(matrix)
    result = bellmanFord(matrixGraph)
    print(result[(79,79)] + matrix[0][0])
      
