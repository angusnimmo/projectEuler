from datetime import datetime
import requests


example = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]


def main():
    start_time = datetime.now()
    matrix = requests.get('https://projecteuler.net/resources/documents/0082_matrix.txt').text
    matrix = matrix.split('\n')
    matrix = matrix[:-1]
    matrix = [[int(j) for j in i.split(',')] for i in matrix]
    n, m = len(matrix), len(matrix[0])
    matrix_graph = make_graph(matrix)
    result = bellman_ford(matrix_graph, (0, 0))
    print(result[(n - 1, m - 1)] + matrix[0][0])
    print(datetime.now() - start_time)


def test():
    start_time = datetime.now()
    n, m = len(example), len(example[0])
    example_graph = make_graph(example)
    result = bellman_ford(example_graph, (0, 0))
    print(result[(n - 1, m - 1)] + example[0][0])
    print(datetime.now() - start_time)
    
    
def make_graph(grid: list[list[int]]) -> dict:
    n = len(grid)
    graph = {}
    
    for i in range(n):
        for j in range(n):
            graph[(i, j)] = {}
            
            # Up
            if i > 0:
                graph[(i, j)][(i - 1, j)] = grid[i - 1][j]
                
            # Down
            if i + 1 < n:
                graph[(i, j)][(i + 1, j)] = grid[i + 1][j]
                
            # Left
            if j > 0:
                graph[(i, j)][(i, j - 1)] = grid[i][j - 1]
                
            # Right
            if j + 1 < n:
                graph[(i, j)][(i, j + 1)] = grid[i][j + 1]
                
    return graph


def bellman_ford(graph: dict, start: tuple) -> dict:
    distance = {}
    vertices = set(x for x in graph.keys())
    
    for vertex in vertices:
        distance[vertex] = float('inf')
        
    distance[start] = 0
    
    for _ in range(len(vertices) - 1):
        for head in graph.keys():
            for tail, weight in graph[head].items():
                if distance[head] + weight < distance[tail]:
                    distance[tail] = distance[head] + weight
                    
    return distance

    
if __name__ == '__main__':
    main()
