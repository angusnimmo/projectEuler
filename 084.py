from datetime import datetime
from random import randint, choice


def main():
    start_time = datetime.now()
    community_chest = [0, 10] + [None] * 14
    chance = [0, 10, 11, 24, 39, 5, 'NR', 'NR', 'NU', '-3'] + [None] * 6
    railways = [5, 15, 25, 35, 45]
    utilities = [12, 28, 42]
    community_chest_squares = [2, 17, 33]
    chance_squares = [7, 22, 36]
    consecutive_doubles = 0
    frequencies = [0] * 40
    current_square = 0
    
    for _ in range(10 ** 6):
        r1, r2 = randint(1, 4), randint(1, 4)
        
        if r1 == r2:
            consecutive_doubles += 1
            
            if consecutive_doubles == 3:
                current_square = 10
                consecutive_doubles = 0
        
        else:
            consecutive_doubles = 0
            current_square = (current_square + r1 + r2) % 40
        
            if current_square == 30:
                current_square = 10
            
            elif current_square in community_chest_squares:
                card = choice(community_chest)
                
                if card:
                    current_square = card
            
            elif current_square in chance_squares:
                card = choice(chance)
                
                if card:
                    if type(card) == int:
                        current_square = card
                    
                    elif card == 'NR':
                        current_square = next(x for x in railways if x > current_square)
                        
                    elif card == 'NU':
                        current_square = next(x for x in utilities if x > current_square)
                        
                    elif card == '-3':
                        current_square -= 3
                        
                        if current_square in community_chest_squares:
                            card = choice(community_chest)
                
                            if card:
                                current_square = card
                                
        current_square %= 40
        frequencies[current_square] += 1
        
    order = sorted(range(len(frequencies)), key=lambda i: frequencies[i])
    print(order[-1], order[-2], order[-3])
    print(datetime.now() - start_time)

    
if __name__ == '__main__':
    main()
