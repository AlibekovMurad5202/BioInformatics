money = int(input())
coins = [int(x) for x in input().split(',')]
min_num_coins = [0] + [-1] * money
for m in range(1, money + 1):
    for coin in coins:
        if m >= coin:
            if min_num_coins[m - coin] + 1 < min_num_coins[m] or min_num_coins[m] == -1:
                min_num_coins[m] = min_num_coins[m - coin] + 1
print(min_num_coins[money])
