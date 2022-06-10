x = list(range(1, 1000))
y = 0

for i in x:
    if (i % 3 == 0) | (i % 5 == 0):
        y += i

print(y)
