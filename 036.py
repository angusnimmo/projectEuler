import itertools

binDig = '01'
decDig = '0123456789'
decPal = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
binPal = [[int('1', 2), int('11', 2), int('101', 2), int('111', 2)]]

# Decimal 2 digits
decPal.append([int(i+i) for i in decDig[1:]])

# Decimal 3 digits
decPal.append([int(i+j+i) for i in decDig[1:] for j in decDig])

# Decimal 4 digits
decPal.append([int(i+j+j+i) for i in decDig[1:] for j in decDig])

# Decimal 5 digits
decPal.append([int(i+j+k+j+i) for i in decDig[1:] for j in decDig for k in decDig])

# Decimal 6 digits
decPal.append([int(i+j+k+k+j+i) for i in decDig[1:] for j in decDig for k in decDig])

for i in range(1, 10):
    binHalf = [''.join(j) for j in itertools.product(binDig, repeat=i)]
    binHalf = ['1'+j for j in binHalf]
    oddBin = [int(j+k+j[::-1], 2) for j in binHalf for k in binDig]
    evenBin = [int(j+j[::-1], 2) for j in binHalf for k in binDig]
    binPal.append(evenBin)
    binPal.append(oddBin)
    
binPal = list(itertools.chain(*binPal))
decPal = list(itertools.chain(*decPal))

dbPal = list(set(binPal).intersection(decPal))

print(sum(dbPal))
