coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(target_sum: int) -> dict[int, int]:
    cashback = 0
    result = []

    while cashback < target_sum:
        possible_coins = [coin for coin in coins if coin <= target_sum - cashback]
        coin = max(possible_coins)
        cashback += coin
        result.append(coin)

    return {coin: result.count(coin) for coin in result}


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    curr = amount
    while curr > 0:
        coin = last_coin[curr]
        result[coin] = result.get(coin, 0) + 1
        curr -= coin

    return dict(sorted(result.items()))



print(find_coins_greedy(113))
print(find_min_coins(113))