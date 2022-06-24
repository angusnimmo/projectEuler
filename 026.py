def fractionToDecimal(numerator, denominator):
    result = ''
    remainderIndex = {}
    remainder = numerator % denominator
    
    while ((remainder != 0) and (remainder not in remainderIndex)):
        remainderIndex[remainder] = len(result)
        remainder *= 10
        digit = remainder // denominator
        result += str(digit)
        remainder %= denominator

    if (remainder == 0):
        return ''

    else:
        return result[remainderIndex[remainder]:]

decimalLength = []

for x in range(1, 1000):
    decLen.append(len(fractionToDecimal(1, x)))
    
print(decLen.index(max(decimalLength)) + 1)
