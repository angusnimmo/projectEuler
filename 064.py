limit = 10000
count = 0

for n in range(2, limit+1):
    # https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf
    # Theorem 2.3
    a0 = int(n**0.5)
    
    if a0**2 == n:
        continue
    else:
        period = 0
        m = 0
        d = 1
        a = a0
        
        # https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/alexajp.pdf
        # Corollary 3.3
        while a != 2*a0:
            m = d*a - m
            d = int((n - m**2)/d)
            a = int((a0+m)/d)
            period += 1
        
        if period%2 == 1:
            count += 1
            
print(count)
