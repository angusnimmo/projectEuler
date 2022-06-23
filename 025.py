def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]
    
index = 1

while len(str(fib(index))) < 1000:
    index += 1

print(index)
