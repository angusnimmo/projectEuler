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
    cost = [matrix[i][-1] for i in range(n)]
    
    for j in range(m - 2, -1, -1):
        cost[0] += matrix[0][j]
        
        for i in range(1, n):
            cost[i] = min(cost[i], cost[i - 1]) + matrix[i][j]
            
        for i in range(n - 2, -1, -1):
            cost[i] = min(cost[i], cost[i + 1] + matrix[i][j])

    print(min(cost))
    print(datetime.now() - start_time)


def test():
    start_time = datetime.now()
    n, m = len(example), len(example[0])
    cost = [example[i][-1] for i in range(n)]
    
    for j in range(m - 2, -1, -1):
        cost[0] += example[0][j]
        
        for i in range(1, n):
            cost[i] = min(cost[i], cost[i - 1]) + example[i][j]
            
        for i in range(n - 2, -1, -1):
            cost[i] = min(cost[i], cost[i + 1] + example[i][j])
    
    print(min(cost))
    print(datetime.now() - start_time)

    
if __name__ == '__main__':
    main()
