def factorial(x):
    total = 1
    for i in range(0, x):
        total *= i+1
    return total
    
# Sum of the factorial of the digits of x, base b
def SFD(x, b):
    total = 0
    while x > 0:
        total += factorial(x % b)
        x //= b
    return total
    
# Let n be a k-digit number, where k >= 8
# => SFD(n) <= 9!*k
# n >= 10**(k-1)
# n >= 10**7 * 10**(k-8)
# [Bernoulli's Inequality: (1+x)**n >= 1+n*x where x is real and x > -1, n is a possitive integer
# => 10**(k-8) >= 1 + 9*(k-8)]
# n >= 10**7 * [1 + 9*(k-8)]
# n > 9!*8*(9k - 71)
# n > 9!*(72k - 71*8)
# n > 9!*k
# => SFD(n) = n can only be true when nMax = 9!*7

factorions = []

for i in range(3, 7*factorial(9)):
    if i == SFD(i, 10):
        factorions.append(i)
        
print(sum(factorions))
