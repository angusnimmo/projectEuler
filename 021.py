x = list(range(1, 10000))
y = []
count = 0

for i in x:
    factors = []
    for j in range(1, i):
        if i % j == 0:
            factors.append(j)
    y.append(sum(factors))
    
for i in range(0, len(x)):
    if x[i] == y[i]:
        continue
    elif y[i] >= len(x):
        continue
    elif x[i] == y[y[i]-1]:
        count += x[i]

print(count)
