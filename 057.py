count = 0

numerator = 3
denominator = 2

for i in range(1000):
    numerator += 2 * denominator
    denominator = numerator - denominator
    
    if len(str(numerator)) > len(str(denominator)):
        count += 1
        
print(count)
