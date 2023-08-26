def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i - 1] <= j: 
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i -1]],dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
maxProfit = knapsack(weights, values, capacity)
print("Maximum Profit:", maxProfit)
