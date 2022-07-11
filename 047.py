from math import sqrt

def primeFactors(n):
    pf = []
    
    while n % 2 == 0:
        pf.append(2)
        n /= 2
        
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            pf.append(i)
            n /= i
            
    if n > 2:
        pf.append(int(n))
        
    return pf
    
if __name__ == "__main__":
    x = 1
    consec = 4
    
    while True:
        if all([len(set(primeFactors(x+i))) >= consec for i in range(consec)]):
            print(x)
            break
            
        x += 1
