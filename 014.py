import time

start = time.time()

def collatz(n):
    steps = []
    while n != 1:
        steps.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    steps.append(n)
    return steps
    
x = list(range(3, 1000000, 2))

y = [len(collatz(i)) for i in x]
ymax = max(y)
ymaxi = y.index(ymax)

print(x[ymaxi], ymax)

stop = time.time()
print(stop - start)
