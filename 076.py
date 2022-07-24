def partitionNumber(n):
    ways = [0] * (n+1)
    ways[0] = 1
    
    for i in range(1, n):
        for j in range(i, n+1):
            ways[j] += ways[j-i]
            
    return ways[-1]
    
if __name__ == "__main__":
    print(partitionNumber(100))
