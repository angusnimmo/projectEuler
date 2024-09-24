from datetime import datetime
from itertools import permutations


def main():
    start_time = datetime.now()
    lines = [gen_line([10] + list(x)) for x in permutations(range(1, 10))]
    lines = [line for line in lines if valid(line)]
    values = [gen_int(line) for line in lines]
    print(max(values))
    print(datetime.now() - start_time)
    
    
def gen_line(p: list[int]) -> list[int]:
    return [
        p[0], p[5], p[6],
        p[1], p[6], p[7],
        p[2], p[7], p[8],
        p[3], p[8], p[9],
        p[4], p[9], p[5]
    ]
    
    
def valid(line: list[int]) -> bool:
    return all(sum(line[i * 3: (i + 1) * 3]) == sum(line[0: 3]) for i in range(5))
    
    
def gen_int(line: list[int]) -> int:
    outers = [line[i * 3] for i in range(5)]
    min_node = min(outers)
    temp = line
    
    for _ in range(line.index(min_node)):
        temp.append(temp.pop(0))
        
    return int(''.join(str(x) for x in temp))


if __name__ == '__main__':
    main()
