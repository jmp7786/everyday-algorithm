class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[float('inf')] * (len(coins)+1) for _ in range(amount+1)]
        memo[0] = [0] * (len(coins)+1)
        for n in range(1, amount+1): 
            for i in range(len(coins)): 
                c = coins[i]
                if n - c >= 0: 
                    if n-c >= 0:
                        memo[n][i] =+ memo[n-c][len(coins)]
                    memo[n][i] += 1
            
            memo[n][len(coins)] = min(memo[n]) 
        # print(memo)
        result = memo[-1][len(coins)]
        return  result if result != float('inf') else -1
        # return 1 