import requests
from collections import Counter

cardValues = '23456789TJQKA'
straights = [set(cardValues[i:i+5]) for i in range(len(cardValues)-4)]

def handRank(hand):
    cards = ''.join([i[0] for i in hand])
    suits = ''.join([i[1] for i in hand])
    
    if (set(cards) == set('TJQKA')) and (len(set(suits)) == 1):#
        # Royal flush
        return 9
    elif (set(cards) in straights) and (len(set(suits)) == 1):
        # Straight flush
        return 8
    elif any([cards.count(cards[i]) == 4 for i in range(2)]):
        # Four of a kind
        return 7
    elif len(set(cards)) == 2:
        # Full house
        return 6
    elif len(set(suits)) == 1:
        # Flush
        return 5
    elif set(cards) in straights:
        # Straight
        return 4
    elif any([cards.count(cards[i]) == 3 for i in range(3)]):
        # Three of a kind
        return 3
    elif len(set(cards)) == 3:
        # Two pairs
        return 2
    elif len(set(cards)) == 4:
        # One pair
        return 1
    else:
        # High card
        return 0
        
def settleEqualRanks(hand):
    cards = ''.join([i[0] for i in hand])
    cardIndices = [cardValues.index(i) for i in cards]
    p1Indices = cardIndices[:5]
    p2Indices = cardIndices[5:]
    p1IndexFreq = Counter(p1Indices).most_common()
    p2IndexFreq = Counter(p2Indices).most_common()
    p1MaxFreq = max([i[1] for i in p1IndexFreq])
    p2MaxFreq = max([i[1] for i in p2IndexFreq])
    p1High = max([i[0] for i in p1IndexFreq if (i[1] == p1MaxFreq)])
    p2High = max([i[0] for i in p2IndexFreq if (i[1] == p2MaxFreq)])
    
    while p1High == p2High:
        p1Indices.remove(p1High)
        p2Indices.remove(p2High)
        p1IndexFreq = Counter(p1Indices).most_common()
        p2IndexFreq = Counter(p2Indices).most_common()
        p1MaxFreq = max([i[1] for i in p1IndexFreq])
        p2MaxFreq = max([i[1] for i in p2IndexFreq])
        p1High = max([i[0] for i in p1IndexFreq if (i[1] == p1MaxFreq)])
        p2High = max([i[0] for i in p2IndexFreq if (i[1] == p2MaxFreq)])
        
    return p1High > p2High

def compareHands(hand):
    p1Rank = handRank(hand[:5])
    p2Rank = handRank(hand[5:])
    
    if p1Rank == p2Rank:
        return settleEqualRanks(hand)
    else:
        return p1Rank > p2Rank

if __name__ == "__main__":
    hands = requests.get('https://projecteuler.net/project/resources/p054_poker.txt').text
    hands = hands.split('\n')
    hands = hands[:-1]
    hands = [i.split(' ') for i in hands]
    p1Count = 0

    for hand in hands:
        if compareHands(hand):
            p1Count += 1
            
    print(p1Count)
