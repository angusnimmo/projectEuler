def digitSum(n):
    return sum([int(i) for i in n])

powers = [str(i**j) for i in range(100) for j in range(100)]

print(max([digitSum(i) for i in powers]))
