class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount+1) for _ in range(len(coins)+1)]
        n = len(coins)
        for i in range(n+1): 
            dp[i][0] = 0
        # print(dp)
        for i in range(1, amount+1): 
            minumum = float('inf')
            for j in range(len(coins)): 
                coin = coins[j]
                if i-coin >=0: 
                    dp[j][i]  =  dp[n][i-coin]+1
                    minumum = min(minumum, dp[j][i])
                
            dp[n][i] = minumum
        # print(dp)
        return dp[n][amount] if dp[n][amount] != float('inf') else -1
[
    [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
    [0, inf, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
    [0, inf, inf, inf, inf, 1, inf, inf, inf, inf, inf, inf], 
    [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]]

