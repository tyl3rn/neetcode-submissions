class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} #key: (i, buying) : maxProfit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying: #buying
                resBuy = dfs(i+1, False) - prices[i]
                cache[(i, True)] = max(resBuy, cooldown)
                return cache[(i, buying)]
            if not buying: #selling 
                resSelling = dfs(i+2, True) + prices[i]
                cache[(i, False)] = max(resSelling, cooldown)
                return cache[(i, False)]
        return dfs(0, True)


            
            
