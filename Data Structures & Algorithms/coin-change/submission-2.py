class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf") for i in range(amount+1)]  
        memo[0] = 0      
        for i in range(1, amount+1):
            
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-coin])
        return memo[-1] if memo[-1] != float("inf") else -1

            
            



                