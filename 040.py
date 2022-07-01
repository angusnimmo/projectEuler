import math

strLen = 0
digits = 0

while digits < 5:
    digits += 1
    strLen += digits * 9 * 10**(digits - 1)
    
intMax = int(1e5 + (round((1e6 - strLen) / 6)))

digStr = ''.join([str(i) for i in range(1, intMax + 1)])

result = math.prod([int(digStr[10**i - 1]) for i in range(0, 7)])

print(result)
