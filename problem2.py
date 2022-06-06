x = np.array([1, 1])
y = 0

while x[-1] < 4e6:
    x = np.append(x, [[x[-1] + x[-2]]])
    
for i in x[:-1]:
    if i % 2 == 0:
        y += i
        
print(y)
