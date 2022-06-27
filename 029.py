import itertools

print(len(set([i[0]**i[1] for i in itertools.product(list(range(2, 101)), repeat=2)])))
