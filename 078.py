from datetime import datetime


def main():
    start_time = datetime.now()
    modulus = int(1e6)
    n = 0
    partitions = [1]

    while partitions[-1] % modulus != 0:
        n += 1
        temp = 0
        k = 1
        g = pentagonal(k)
        
        while g <= n:
            temp += (((-1) ** (k - 1)) * partitions[n - g]) % modulus
            k *= -1
            
            if k > 0:
                k += 1
                
            g = pentagonal(k)
            
        partitions.append(temp % modulus)
    
    print(n)
    print(datetime.now() - start_time)
    
    
def pentagonal(n: int) -> int:
    return (n * (3 * n - 1)) // 2


if __name__ == '__main__':
    main()
