import itertools

x = itertools.permutations('0123456789')

y = [''.join(str(i) for i in j) for j in x]

print(y[999999])
