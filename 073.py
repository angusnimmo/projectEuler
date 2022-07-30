def farey_sequence_count(limit):
    count = 0
    (a, b, c, d) = (1, 3, limit//3, limit-1)
    
    while not (c == 1 and d == 2):
        k = (limit+b)//d
        (a, b, c, d) = (c, d, k*c - a, k*d - b)
        count += 1
            
    return count

def main():
    print(farey_sequence_count(12000))
    
if __name__ == "__main__":
    main()
