coins = [1, 2, 5, 10 , 20, 50, 100, 200]
total = 200
ways = [0] * (total + 1)
ways[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], total + 1):
        ways[j] += ways[j - coins[i]]

print(ways[-1])
