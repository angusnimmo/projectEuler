from datetime import datetime


def main():
    start_time = datetime.now()
    L = 1500000
    visited = [False] * (L + 1)
    hash_table = {}

    for m in range(2, int((L // 2) ** .5) + 1):
        for n in range(1, m):
            c = (m ** 2) + (n ** 2)
            a, b = sorted([(m ** 2) - (n ** 2), 2 * m * n])
            l = a + b + c
            
            if l > L:
                continue
            
            if not visited[l]:
                hash_table[l] = {(a, b)}
                visited[l] = True
                
                for k in range(2, (L // l) + 1):
                    kl = k * l
                    ka = k * a
                    kb = k * b
                    
                    if not visited[kl]:
                        hash_table[kl] = {(ka, kb)}
                        visited[kl] = True
                    else:
                        hash_table[kl].add((ka, kb))
                        
            else:
                hash_table[l].add((a, b))
                
                for k in range(2, (L // l) + 1):
                    kl = k * l
                    ka = k * a
                    kb = k * b
                    
                    if not visited[kl]:
                        hash_table[kl] = {(ka, kb)}
                        visited[kl] = True
                    else:
                        hash_table[kl].add((ka, kb))
                
    count = 0

    for x in hash_table:
        if len(hash_table[x]) == 1:
            count += 1
            
    print(count)
    print(datetime.now() - start_time)     
            

if __name__ == '__main__':
    main()
