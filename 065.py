def e_cont_frac(n):
    sequence = [2*(i+1)//3 if (i%3 == 2) else 1 for i in range(n)]
    sequence[0] += 1
    return sequence
    
def e_frac(n):
    sequence = e_cont_frac(n)
    num = 1
    den = 0
    
    for i in reversed(sequence):
        temp = num
        num = den + (num * i)
        den = temp
        
    return (num, den)
    
if __name__ == "__main__":
    print(sum([int(i) for i in str(e_frac(100)[0])]))
