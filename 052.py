import itertools

def condition(x):
    if all([sorted(str(i*x)) == sorted(str(x)) for i in range(1, 7)]):
        return True
    return False

if __name__ == "__main__":
    digits = '123456789'
    nDigits = 1
    solutions = []
    
    while len(solutions) < 1:
        nDigits += 1
        solutions.append([int(''.join(i)) for i in list(itertools.product(digits, repeat=nDigits)) if condition(int(''.join(i)))])
        solutions = list(itertools.chain.from_iterable(solutions))
        
    print(solutions)
