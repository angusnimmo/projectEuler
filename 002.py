x = [1, 1]
y = 0

while x[-1] < 4e6:
    x.append(x[-1] + x[-2])
    
for i in x[:-1]:
    if i % 2 == 0:
        y += i
        
print(y)
