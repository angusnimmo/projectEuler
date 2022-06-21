import itertools
import math

x = list(range(1, 28124))

def abnCheck(n):
    factors = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            if i != n/i:
                factors.append(n/i)
    if sum(factors) > n:
        return True
    else:
        return False
       
abn = [12]

for i in range(13, 28124):
    if abnCheck(i) == True:
        abn.append(i)
        
abn2 = [sum(i) for i in itertools.combinations_with_replacement(abn, 2)]
result = sum(list(set(x) - set(abn2)))

print(result)
