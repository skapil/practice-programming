import math


def minimum_coins(coins, value):
    min_coins: list = [0] * (value + 1)
    min_coins[0] = 1
    coins_set: set = set(coins)

    for idx in range(1, len(min_coins)):
        if idx in coins_set:
            min_coins[idx] = 1
        else:
            cur_min_coin = math.inf
            for coin in coins_set:
                if coin <= idx:
                    cur_min_coin = min(cur_min_coin, min_coins[idx - coin])
            min_coins[idx] = cur_min_coin + 1

    return min_coins[-1]


def ways_to_climb_stairs(stairs: int) -> int:
    ways: list = [0] * (stairs + 2)

    ways[0], ways[1], ways[2] = 0, 1, 2
    for idx in range(2, len(ways)):
        ways[idx] = ways[idx - 1] + ways[idx - 2]
    return ways[-1]


if __name__ == '__main__':
    print(ways_to_climb_stairs(5))
