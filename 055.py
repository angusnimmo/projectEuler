def isPalindrome(n):
    return all([str(n)[i] == str(n)[-i-1] for i in range(len(str(n)))])
    
def reverseAdd(nList):
    nReversed = int(str(nList[-1])[::-1])
    nList += [nReversed, nReversed + nList[-1]]
    
def lychrelList(limit):
    lychrelNumbers = [True] * limit
    lychrelNumbers[0] = False
    
    for i in range(limit):
        if not lychrelNumbers[i]:
            continue
        
        path = [i]
        
        for j in range(50):
            reverseAdd(path)
            
            if isPalindrome(path[-1]):
                for k in path[:-1]:
                    if (k < limit) and (k >= i):
                        lychrelNumbers[k] = False
                        
                break
                
    return [i for (i, isLychrel) in enumerate(lychrelNumbers) if isLychrel]

if __name__ == "__main__":
    print(len(lychrelList(10000)))
