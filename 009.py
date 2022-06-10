from math import sqrt

for i in range(1, 1000):
    for j in range(1, 1000):
        if 2 * i * j - 2000 * (i + j) + 1000000 == 0:
            x = [i, j]
            break
            
print(x[0] * x[1] * sqrt(x[0]**2 + x[1]**2))
