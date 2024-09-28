from datetime import datetime


def main():
    start_time = datetime.now()
    square = [False] * 101
    count = 0
    
    for i in range(1, 11):
        square[i ** 2] = True
        
    for i in range(2, 100):
        if not square[i]:
            count += sum(int(x) for x in str(newton_root(i))[:100])
        
    print(count)
    print(datetime.now() - start_time)
    
    
def newton_root(n: int) -> str:
    n *= 10 ** 204
    x1 = int(n ** .5)
    x0 = x1 - 2

    while abs(x1 - x0) > 1:
        x0 = x1
        x1 = (x0 // 2) + (n // (2 * x0))
        
    return str(x1)
    
    
if __name__ == '__main__':
    main()
