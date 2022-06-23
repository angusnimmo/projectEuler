x = [1, 1]
index = 2

while len(str(x[-1])) < 1000:
    x.append(x[-1] + x[-2])
    del x[:-3]
    index += 1

print(index)
