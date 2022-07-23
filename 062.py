if __name__ == "__main__":
    flag = True
    order = 7

    while flag:
        cubes = [i**3 for i in range(int(10**(order/3)), int(10**((order+1)/3))+1)]
        sortedStrings = [''.join(sorted(str(i))) for i in cubes]
        mostFrequent = max(set(sortedStrings), key = sortedStrings.count)
        
        if sortedStrings.count(mostFrequent) >= 5:
            cubeRoot = int(10**(order/3)) + sortedStrings.index(mostFrequent)
            print(cubeRoot, cubeRoot**3)
            break
        else:
            order += 1
