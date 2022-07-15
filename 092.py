def squareDigits(x):
    return sum([int(i)**2 for i in str(x)])
    
def count89(limit):
    is1 = [False] * limit
    is89 = [False] * limit
    is1[1] = True
    is89[89] = True
    
    for i in range(1, limit):
        if (is1[i] == True) or (is89[i] == True):
            continue
            
        chain = [i]
        
        while True:
            chain.append(squareDigits(chain[-1]))
            
            if chain[-1] < limit:
                if is1[chain[-1]]:
                    for j in chain:
                        if j < limit:
                            is1[j] = True
                            
                    break
                    
                if is89[chain[-1]]:
                    for j in chain:
                        if j < limit:
                            is89[j] = True
                            
                    break
            
    return len([i for (i, is89Chain) in enumerate(is89) if is89Chain])
    
if __name__ == "__main__":
    print(count89(10000000))
