def best_time_to_sell_and_buy_stock_iterative(prices):
    """
    One-pass optimal solution.
    Time: O(n)
    Space: O(1)
    """
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

def best_time_to_sell_and_buy_stock_brute_force(prices):
    """
    Brute force solution.
    Time: O(n^2)
    Space: O(1)
    """
    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit

def best_time_to_sell_and_buy_stock_two_pointers(prices):
    """
    Two pointers solution.
    Time: O(n)
    Space: O(1)
    """
    if len(prices) < 2:
        return 0

    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            max_profit = max(max_profit, prices[right] - prices[left])
        else:
            left = right
        right += 1

    return max_profit