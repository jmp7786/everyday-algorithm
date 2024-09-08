class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount+1) for _ in range(len(coins)+1)]
        n = len(coins)
        for i in range(n+1): 
            dp[i][0] = 0
        for i in range(1, amount+1): 
            minumum = float('inf')
            for j in range(len(coins)): 
                coin = coins[j]
                if i-coin >=0: 
                    dp[j][i]  =  dp[n][i-coin]+1
                    minumum = min(minumum, dp[j][i])
                
            dp[n][i] = minumum

        return dp[n][amount] if dp[n][amount] != float('inf') else -1
