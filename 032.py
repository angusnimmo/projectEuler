import itertools

digits = [''.join(i) for i in list(itertools.permutations('123456789'))]
solutions = []

for i in digits:
    for j in range(1, 7):
        for k in range(j+1, 8):
            if int(i[:j]) * int(i[j:k]) == int(i[k:]):
                solutions.append(int(i[k:]))

print(sum(list(set(solutions))))
