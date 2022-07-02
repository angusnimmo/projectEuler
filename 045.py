def triangle(n):
    return int(n*(n+1)/2)
    
def pentagon(n):
    return int(n*((3*n)-1)/2)
    
def hexagon(n):
    return int(n*((2*n)-1))
    
order = 1

triArr = [triangle(i) for i in range(2, 10**order)]
pentArr = [pentagon(i) for i in range(2, 10**order)]
hexArr = [hexagon(i) for i in range(2, 10**order)]

result = set(triArr).intersection(set(pentArr), set(hexArr))

while len(result) < 2:
    order += 1
    triArr = [triangle(i) for i in range(2, 10**order)]
    pentArr = [pentagon(i) for i in range(2, 10**order)]
    hexArr = [hexagon(i) for i in range(2, 10**order)]
    result = set(triArr).intersection(set(pentArr), set(hexArr))
    
print(result)
