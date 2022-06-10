import math

n = 600851475143
pf = []

while n % 2 == 0:
    pf.append(2)
    n /= 2
    
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        pf.append(i)
        n /= i
        
if n > 2:
    pf.append(n)
    
print(pf)
