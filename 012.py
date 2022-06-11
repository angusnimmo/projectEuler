from math import sqrt

tri = [1]
nFactors = 1

while nFactors < 500:
    nFactors = 0
    x = len(tri) + 1
    tri.append(x * (x + 1) / 2)
    for i in range(1, int(sqrt(tri[-1]))):
        if tri[-1] % i == 0:
            nFactors += 2
            
print(tri[-1])
