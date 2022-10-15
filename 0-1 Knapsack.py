def knapSack(maxWeight, weights, values, size):
    dp = [[0 for x in range(maxWeight + 1)] for x in range(size + 1)]
    
    for i in range(size + 1):
        for w in range(maxWeight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
  
    return dp[size][maxWeight]
  
values = [50,100,150,200]
weights = [8,16,32,40]
maxWeight = 64
print(knapSack(maxWeight, weights, values, len(values)))
