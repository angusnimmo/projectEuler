import itertools

x = [i[0] * i[1] for i in list(itertools.combinations_with_replacement(list(range(900, 1000)), 2))]

def digit(number, n):
    return number // 10**n % 10

for i in x:
    if (digit(i, 0) == digit(i, 5)) & (digit(i, 1) == digit(i, 4)) & (digit(i, 2) == digit(i, 3)):
        print(i)
