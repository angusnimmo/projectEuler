import itertools

def concatenatedProduct(x):
    return ''.join([str(i*x) for i in range(1, (9//len(str(x)))+1)])

pandigitals = [''.join(i) for i in itertools.permutations('123456789')]
solutions = [concatenatedProduct(i) for i in range(1, 9999)]

print(max(list(set(pandigitals) & set(solutions))))
